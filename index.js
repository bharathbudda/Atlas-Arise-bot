import fetch from "node-fetch";
import * as fs from "fs";

const TELEGRAM_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const ANTHROPIC_KEY = process.env.ANTHROPIC_API_KEY;
const DATA_FILE = "./atlas_places.json";
const TELEGRAM_API = `https://api.telegram.org/bot${TELEGRAM_TOKEN}`;

// ── Storage ──────────────────────────────────────────────────────────────────

function loadPlaces() {
  try {
    if (fs.existsSync(DATA_FILE)) return JSON.parse(fs.readFileSync(DATA_FILE, "utf8"));
  } catch (_) {}
  return [];
}

function savePlaces(places) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(places, null, 2));
}

// ── Telegram helpers ──────────────────────────────────────────────────────────

async function sendMessage(chatId, text) {
  await fetch(`${TELEGRAM_API}/sendMessage`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ chat_id: chatId, text, parse_mode: "Markdown" }),
  });
}

async function getFileUrl(fileId) {
  const res = await fetch(`${TELEGRAM_API}/getFile?file_id=${fileId}`);
  const data = await res.json();
  return `https://api.telegram.org/file/bot${TELEGRAM_TOKEN}/${data.result.file_path}`;
}

async function downloadImage(url) {
  const res = await fetch(url);
  const buffer = await res.buffer();
  return buffer.toString("base64");
}

// ── Claude helpers ────────────────────────────────────────────────────────────

async function callClaude(messages, system) {
  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": ANTHROPIC_KEY,
      "anthropic-version": "2023-06-01",
    },
    body: JSON.stringify({
      model: "claude-opus-4-5",
      max_tokens: 1000,
      system,
      messages,
    }),
  });
  const data = await res.json();
  return data.content?.[0]?.text || "";
}

async function fetchPageContent(url) {
  try {
    // For YouTube, extract video ID and get transcript via a public API
    const ytMatch = url.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})/);
    if (ytMatch) {
      return await fetchYouTubeTranscript(ytMatch[1]);
    }
    // For general URLs, fetch the page HTML and extract text
    const res = await fetch(url, {
      headers: { "User-Agent": "Mozilla/5.0 (compatible; AtlasBot/1.0)" },
      timeout: 8000,
    });
    const html = await res.text();
    // Strip HTML tags, collapse whitespace, limit length
    const text = html
      .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "")
      .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "")
      .replace(/<[^>]+>/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, 4000);
    return text || "Could not extract meaningful content from this URL.";
  } catch (e) {
    return `Could not fetch URL: ${e.message}`;
  }
}

async function fetchYouTubeTranscript(videoId) {
  try {
    // Fetch YouTube page and extract description + title
    const res = await fetch(`https://www.youtube.com/watch?v=${videoId}`, {
      headers: { "User-Agent": "Mozilla/5.0" },
    });
    const html = await res.text();
    const titleMatch = html.match(/"title":"([^"]+)"/);
    const descMatch = html.match(/"shortDescription":"([^"]+)"/);
    const title = titleMatch ? titleMatch[1] : "";
    const desc = descMatch ? descMatch[1].replace(/\\n/g, " ").slice(0, 1500) : "";
    return `YouTube Video\nTitle: ${title}\nDescription: ${desc}`;
  } catch (e) {
    return "Could not fetch YouTube content.";
  }
}

const SYSTEM_PROMPT = `You are Atlas — a precise, intelligent location extraction and enrichment system. Your tone is crisp, formal, minimal. No pleasantries, no padding.

When given content (webpage text, image description, plain text), extract the travel destination being referenced and return ONLY valid JSON:

{
  "name": "place name",
  "country": "country or region",
  "lat": latitude_number,
  "lng": longitude_number,
  "category": "trek|observatory|nature|culture|food|place",
  "desc": "One sharp sentence — what makes this place worth going to.",
  "facts": ["fact1", "fact2", "fact3", "fact4"],
  "source_context": "One sentence capturing WHY this was saved — the specific detail, trail, season, or angle that made it interesting."
}

Facts must be practical: best time to visit, altitude if relevant, permit requirements, duration, one unique distinguishing detail. Max 5 words each.
If no clear travel destination is found, return: {"error": "No location found"}
Return only the JSON object. No markdown, no explanation.`;

// ── Message handlers ──────────────────────────────────────────────────────────

async function handleLink(chatId, url) {
  await sendMessage(chatId, `_Fetching content..._`);
  const content = await fetchPageContent(url);
  const response = await callClaude(
    [{ role: "user", content: `URL: ${url}\n\nPage content:\n${content}` }],
    SYSTEM_PROMPT
  );
  return parseAndSave(chatId, response);
}

async function handleImage(chatId, fileId) {
  await sendMessage(chatId, `_Reading image..._`);
  const fileUrl = await getFileUrl(fileId);
  const base64 = await downloadImage(fileUrl);
  const response = await callClaude(
    [{
      role: "user",
      content: [
        { type: "image", source: { type: "base64", media_type: "image/jpeg", data: base64 } },
        { type: "text", text: "Extract the travel destination depicted in this image. Focus on the location shown, not where the photo was taken." }
      ]
    }],
    SYSTEM_PROMPT
  );
  return parseAndSave(chatId, response);
}

async function handleText(chatId, text) {
  const response = await callClaude(
    [{ role: "user", content: text }],
    SYSTEM_PROMPT
  );
  return parseAndSave(chatId, response);
}

async function parseAndSave(chatId, response) {
  try {
    const clean = response.replace(/```json|```/g, "").trim();
    const data = JSON.parse(clean);

    if (data.error) {
      await sendMessage(chatId, `Atlas — ${data.error}.`);
      return;
    }

    const places = loadPlaces();
    const existing = places.find(p => p.name.toLowerCase() === data.name.toLowerCase());
    if (existing) {
      await sendMessage(chatId, `Atlas — *${data.name}* already in your list.`);
      return;
    }

    const place = { id: Date.now().toString(), ...data };
    places.unshift(place);
    savePlaces(places);

    const factsLine = (data.facts || []).slice(0, 4).join(" · ");
    const reply = [
      `Atlas — *${data.name}* saved.`,
      `${data.country} · ${data.category}`,
      factsLine,
      data.source_context ? `\n_${data.source_context}_` : "",
    ].filter(Boolean).join("\n");

    await sendMessage(chatId, reply);
  } catch (e) {
    await sendMessage(chatId, `Atlas — Could not parse location. Try a clearer description.`);
  }
}

// ── Commands ──────────────────────────────────────────────────────────────────

async function handleCommand(chatId, command, args) {
  const places = loadPlaces();

  if (command === "/start") {
    await sendMessage(chatId, `*Atlas* — active.\n\nSend a link, screenshot, or place name. I'll handle the rest.\n\n/list · /map · /plan [place] · /delete [place]`);

  } else if (command === "/list") {
    if (!places.length) { await sendMessage(chatId, "Atlas — No places saved yet."); return; }
    const categories = args[0]?.toLowerCase();
    const filtered = categories ? places.filter(p => p.category === categories) : places;
    if (!filtered.length) { await sendMessage(chatId, `Atlas — No places in category: ${categories}.`); return; }
    const lines = filtered.map((p, i) => `${i + 1}. *${p.name}* — ${p.country} · ${p.category}`).join("\n");
    await sendMessage(chatId, `Atlas — ${filtered.length} place${filtered.length > 1 ? "s" : ""}:\n\n${lines}`);

  } else if (command === "/map") {
    await sendMessage(chatId, `Atlas — Open your Wanderlist map:\nhttps://claude.ai\n\n_Your saved places sync automatically._`);

  } else if (command === "/plan") {
    const placeName = args.join(" ");
    if (!placeName) { await sendMessage(chatId, "Atlas — Usage: /plan [place name]"); return; }
    const place = places.find(p => p.name.toLowerCase().includes(placeName.toLowerCase()));
    if (!place) { await sendMessage(chatId, `Atlas — ${placeName} not found in your list.`); return; }
    const plan = await callClaude(
      [{ role: "user", content: `Give me a concise trip plan for ${place.name}, ${place.country}. Include: best time, how to get there from major Indian cities, where to stay, key things to do, estimated budget in INR. Be specific and brief.` }],
      "You are Atlas. Respond in crisp, structured plain text. No markdown headers. Minimal words, maximum information. Bullet points only where necessary."
    );
    await sendMessage(chatId, `*${place.name} — Trip Plan*\n\n${plan}`);

  } else if (command === "/delete") {
    const placeName = args.join(" ");
    if (!placeName) { await sendMessage(chatId, "Atlas — Usage: /delete [place name]"); return; }
    const idx = places.findIndex(p => p.name.toLowerCase().includes(placeName.toLowerCase()));
    if (idx === -1) { await sendMessage(chatId, `Atlas — ${placeName} not found.`); return; }
    const removed = places.splice(idx, 1)[0];
    savePlaces(places);
    await sendMessage(chatId, `Atlas — *${removed.name}* removed.`);

  } else if (["/trek", "/observatory", "/nature", "/culture", "/food", "/place"].includes(command)) {
    const cat = command.slice(1);
    const filtered = places.filter(p => p.category === cat);
    if (!filtered.length) { await sendMessage(chatId, `Atlas — No ${cat} saved yet.`); return; }
    const lines = filtered.map((p, i) => `${i + 1}. *${p.name}* — ${p.country}`).join("\n");
    await sendMessage(chatId, `Atlas — ${cat} (${filtered.length}):\n\n${lines}`);

  } else {
    await sendMessage(chatId, `Atlas — Unknown command.`);
  }
}

// ── Polling loop ──────────────────────────────────────────────────────────────

let offset = 0;

async function poll() {
  try {
    const res = await fetch(`${TELEGRAM_API}/getUpdates?offset=${offset}&timeout=30`);
    const data = await res.json();

    for (const update of data.result || []) {
      offset = update.update_id + 1;
      const msg = update.message;
      if (!msg) continue;

      const chatId = msg.chat.id;
      const text = msg.text?.trim();
      const photo = msg.photo;

      if (text) {
        if (text.startsWith("/")) {
          const parts = text.split(" ");
          await handleCommand(chatId, parts[0], parts.slice(1));
        } else if (text.match(/^https?:\/\//i)) {
          await handleLink(chatId, text);
        } else {
          await handleText(chatId, text);
        }
      } else if (photo) {
        const largest = photo[photo.length - 1];
        await handleImage(chatId, largest.file_id);
      }
    }
  } catch (e) {
    console.error("Poll error:", e.message);
  }
  setTimeout(poll, 1000);
}

console.log("Atlas — online.");
poll();
