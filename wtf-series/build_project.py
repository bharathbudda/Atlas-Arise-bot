"""Builds the single project file (index.html) and a compact review copy (REVIEW.md)
from one source of truth, so the page and the double-check review never drift apart."""
import html, pathlib, re

ROOT = pathlib.Path(__file__).parent
SCRIPTS = ROOT / "scripts"
SIGNOFF = "Wait… that's a fact."
WPM = 155

STYLE_BLOCK = (
    "Flat 2D editorial explainer illustration in the 'WTF night-notebook' style: clean hand-drawn "
    "white chalk outlines with a slight wobble, flat fills in only warm orange (#FF8C1A), dark navy "
    "(#13213C) and soft slate blue (#6F84A8), with white highlights and a subtle chalk grain. Solid flat "
    "dark navy background (#13213C), no grid. One clear subject with bold, simple shapes and generous empty "
    "space, centred in a vertical 9:16 frame with the top 15% and bottom 30% left empty. No text, letters, "
    "numbers, logos or watermark. No photorealism, 3D, gradients or drop shadows.")
MOTION_BLOCK = (
    "Animate this exact illustration. Keep the art style, line work, colours and composition identical: "
    "flat 2D, chalk outlines, navy background. Smooth, gentle motion only; no camera shake, no new objects, "
    "no text, no morphing of the main subject.")

# ---------------------------------------------------------------- episodes
EPS = [
 dict(n="01", slug="gps", cat="TECH", title="Your phone's map only works because Einstein was right",
  yt="Your GPS needs Einstein to work 🛰️ #shorts",
  cover="YOUR GPS NEEDS EINSTEIN", src_site="Historical Tech Tree",
  facts=[
   ("GPS satellite clocks gain ~38 µs/day net: about +45.7 µs from weaker gravity (general relativity) and about −7.1 µs from orbital speed (special relativity).", "Ashby, Physics Today 2002"),
   ("Uncorrected, one day's drift equals more than 11 km of ranging error (38 µs × speed of light ≈ 11.4 km).", "Ashby, Physics Today 2002"),
   ("Satellite clocks are pre-set before launch to 10.22999999543 MHz instead of 10.23 MHz so that they tick correctly once in orbit.", "ICD-GPS-200; Penn State GEOG 862"),
   ("Orbit altitude about 20,200 km; orbital speed about 3.9 km/s.", "gps.gov"),
  ],
  avoid=["Do not say 'your phone corrects for relativity'. The satellite clocks are offset before launch.",
         "Do not present '10 km/day' as an exact position drift. Say 'more than ten kilometres of error'."],
  sources=["https://physicstoday.aip.org/features/relativity-and-the-global-positioning-system",
           "https://courses.ems.psu.edu/geog862/node/1714", "https://www.gps.gov/systems/gps/space/"],
  shots=[
   ("0–3", "AI clip C1 (from S1)", "Earth seen from space with one GPS satellite on a dashed orbit; thin signal arcs reach a small orange map pin on the globe.", "satellite glides along the dashed orbit; signal rings pulse from satellite toward the pin"),
   ("3–8", "AI still S2", "A hand holding a smartphone showing a simple abstract map with one glowing orange location dot.", None),
   ("8–13", "AI still S3", "Four satellites spaced around Earth, dashed lines converging on one point on the surface.", None),
   ("13–20", "AI clip C2 (from S4)", "A round clock floating above Earth; beneath Earth a curved spacetime grid dips like a stretched sheet.", "the curved grid gently ripples outward and the clock hands sweep slightly faster"),
   ("20–26", "AI still S5", "A GPS satellite streaking past with speed lines behind it, a small clock on its body.", None),
   ("26–33", "LOCAL diagram D1", "Bar chart: +45 (gravity), −7 (speed), +38 net, in microseconds per day.", None),
   ("33–40", "LOCAL diagram D2", "Map with the dot drifting along a growing line: 38 µs × light speed ≈ 11 km.", None),
   ("40–46", "AI still S6", "An engineer's hand turning a tiny dial on a satellite clock in a clean room, a rocket silhouette in the background.", None),
   ("46–53", "AI still S7", "A person walking down a city street at dusk looking at a phone, a glowing orange dot trail behind them.", None),
   ("53–56", "LOCAL end card", "Logo flip and the sign-off.", None),
  ]),
 dict(n="02", slug="whale", cat="EVOLUTION", title="A whale's closest living relative is a hippo",
  yt="A whale's closest living relative is a HIPPO 🦛🐋 #shorts",
  cover="A WHALE'S COUSIN IS A HIPPO", src_site="OneZoom",
  facts=[
   ("Retrotransposon (SINE/LINE) insertions shared at the same loci group hippos with cetaceans and exclude ruminants.", "Nikaido, Rooney & Okada 1999, PNAS 96:10261"),
   ("2001 fossils of early legged whales (pakicetids; Rodhocetus, Artiocetus) show the double-pulley astragalus diagnostic of artiodactyls.", "Thewissen et al. 2001, Nature 413:277; Gingerich et al. 2001, Science 293:2239"),
   ("Whales and hippos share an ancestor that lived roughly 50–60 million years ago; hippo fossils only reach back about 20 million years.", "Boisserie et al. 2005, PNAS"),
  ],
  avoid=["Never say whales evolved from hippos.", "Keep the word 'living'. The closest extinct relatives are raoellids such as Indohyus."],
  sources=["https://pmc.ncbi.nlm.nih.gov/articles/PMC17876", "https://newsarchive.berkeley.edu/news/media/releases/2005/01/24_hippos.shtml"],
  shots=[
   ("0–3", "AI clip C1 (from S1)", "Split scene: a hippo standing in a river on the left, a whale breaching from the ocean on the right, a shoreline between them.", "the whale rises and splashes back; the hippo flicks its ears and blinks"),
   ("3–6", "AI still S2", "A shark and a seal side by side, looking puzzled.", None),
   ("6–10", "AI still S3", "A hand-drawn tree of life branching upward, small animal silhouettes at the branch tips.", None),
   ("10–22", "AI clip C2 (from S4)", "A DNA double helix with small orange segments hovering beside it.", "the orange segments hop into matching slots in the helix one by one"),
   ("22–27", "LOCAL diagram D1", "Cladogram: whales + hippos joined, then cows/deer, then pigs and camels, with orange insertion marks on the shared branch.", None),
   ("27–35", "AI still S5", "Fossil skeleton of a small, wolf-sized, four-legged early whale embedded in layered rock.", None),
   ("35–40", "LOCAL diagram D2", "Simplified ankle bone with two pulley grooves highlighted in orange.", None),
   ("40–47", "AI still S6", "A small hoofed mammal standing at a riverbank at dawn, the shared ancestor, its silhouette faint.", None),
   ("47–54", "AI still S7", "A hippo submerged up to its eyes in a river; its reflection on the water is the silhouette of a whale.", None),
   ("54–57", "LOCAL end card", "Logo flip and the sign-off.", None),
  ]),
 dict(n="03", slug="notes", cat="MUSIC", title="Why music has 12 notes",
  yt="Why does music have exactly 12 notes? 🎹 #shorts",
  cover="WHY 12 NOTES?", src_site="Musicmap",
  facts=[
   ("(3/2)^12 ≈ 129.746 versus 2^7 = 128. The gap is the Pythagorean comma, about 23.46 cents.", "Calculated; standard tuning theory"),
   ("A pure fifth is 701.955 cents; the 12-TET fifth is 700 cents, about 1.96 cents narrower.", "Calculated"),
   ("12-TET was worked out independently by Zhu Zaiyu (1584) and Simon Stevin (about 1585).", "Needham, Science and Civilisation in China, vol. 4"),
   ("Other systems: Indian theory has 22 shrutis; Javanese gamelan uses slendro (5 tones) and pelog (7 tones).", "Standard references"),
  ],
  avoid=["Do not say twelve fifths 'close the circle' exactly.", "Do not credit Pythagoras or Bach with inventing the 12-note or equal-tempered scale."],
  sources=["https://en.wikipedia.org/wiki/Pythagorean_comma", "https://en.wikipedia.org/wiki/12_equal_temperament", "https://en.wikipedia.org/wiki/Shruti_(music)"],
  shots=[
   ("0–3", "AI clip C1 (from S1)", "A piano keyboard seen from above, one octave of twelve keys glowing orange.", "the twelve keys press down one after another in a wave, soft light pulsing"),
   ("3–8", "AI still S2", "A single string stretched on a wooden board (monochord), a finger plucking it, faint vibration curves.", None),
   ("8–20", "LOCAL diagram D1", "Waveforms: ratio 2:1 (octave) and 3:2 (fifth), each with a real tone played (generated locally).", None),
   ("20–28", "AI clip C2 (from S3)", "A spiral staircase of twelve steps winding upward through seven floors, a small orange ball on the bottom step.", "the ball hops up the spiral steps and lands slightly past the top floor's edge"),
   ("28–35", "LOCAL diagram D2", "129.7 vs 128 bars with the small gap labelled 'Pythagorean comma'.", None),
   ("35–41", "AI still S4", "A piano tuner with a tuning lever leaning into an open upright piano, nineteenth-century clothes.", None),
   ("41–45", "AI still S5", "A sitar and a tanpura resting on a patterned rug.", None),
   ("45–49", "AI still S6", "A row of bronze gamelan metallophones with mallets.", None),
   ("49–54", "AI still S7", "A cartoon ear and a piano keyboard shaking hands.", None),
   ("54–57", "LOCAL end card", "Logo flip and the sign-off.", None),
  ]),
 dict(n="04", slug="bacteria", cat="BIOLOGY", title="You are not 90% bacteria",
  yt="You are NOT 90% bacteria 🦠 #shorts",
  cover="YOU ARE NOT 90% BACTERIA", src_site="Size of Life",
  facts=[
   ("A 70 kg reference man has about 3.0×10¹³ human cells and about 3.8×10¹³ bacteria, a ratio of about 1.3:1 (±25%).", "Sender, Fuchs & Milo 2016, PLoS Biol 14:e1002533"),
   ("Bacterial mass is about 0.2 kg; red blood cells are about 84% of human cells by count.", "Sender et al. 2016"),
   ("The 10:1 figure traces to Luckey 1972, a rough estimate.", "Sender et al. 2016"),
   ("One defecation removes about 1/4 to 1/3 of colon bacteria, enough to flip the ratio.", "Sender et al. 2016"),
   ("The authors were at the Weizmann Institute (Israel) and SickKids, Toronto (Canada).", "ScienceDaily, 28 Jan 2016"),
  ],
  avoid=["Never say 'bacteria outnumber us 10 to 1' as a fact, or that we are mostly bacteria by weight."],
  sources=["https://pmc.ncbi.nlm.nih.gov/articles/PMC4991899/", "https://www.sciencedaily.com/releases/2016/01/160128132026.htm"],
  shots=[
   ("0–3", "AI clip C1 (from S1)", "A human silhouette outline filled with hundreds of tiny orange rod- and dot-shaped bacteria.", "the bacteria swirl slowly inside the silhouette like a gentle current"),
   ("3–8", "LOCAL diagram D0", "'10 : 1' stamped, then struck through in orange.", None),
   ("8–13", "AI still S2", "A 1970s desk with a typewriter, a coffee mug and a sheet of abstract scribbled calculations.", None),
   ("13–20", "AI still S3", "A scientist at a microscope, tally marks floating in the air beside them.", None),
   ("20–27", "AI clip C2 (from S4)", "A stylised winding intestine tube, friendly and non-gory, filled with tiny orange bacteria.", "the bacteria drift slowly along the winding tube"),
   ("27–33", "LOCAL diagram D1", "Bars: 38 trillion bacteria vs 30 trillion human cells, ratio ≈ 1.3 : 1.", None),
   ("33–37", "LOCAL diagram D2", "Donut chart: red blood cells 84% of human cells.", None),
   ("37–43", "AI still S5", "An old balance scale: a single mango on one pan, a small heap of tiny orange bacteria on the other, level.", None),
   ("43–49", "AI still S6", "A seesaw with a cartoon human on one end and a cloud of bacteria on the other, the human's side just touching down.", None),
   ("49–54", "AI still S7", "The same human silhouette standing confidently, glowing softly, a few bacteria orbiting around it.", None),
   ("54–57", "LOCAL end card", "Logo flip and the sign-off.", None),
  ]),
 dict(n="05", slug="ok", cat="LANGUAGE", title="OK started as a joke",
  yt="'OK' started as a JOKE in 1839 📰 #shorts",
  cover="OK WAS A JOKE", src_site="The Language Nerds / Mental Floss",
  facts=[
   ("First known print use: Boston Morning Post, 23 March 1839, 'o.k.—all correct—', playing on the misspelling 'oll korrect'.", "Allen Walker Read, American Speech 38 (1963); Merriam-Webster"),
   ("It came from an 1838–39 Boston fad of abbreviated misspellings (O.W. 'oll wright', K.G. 'know go').", "Merriam-Webster; Read 1963–64"),
   ("1840: supporters of Martin Van Buren ('Old Kinderhook') formed O.K. Clubs, which spread the term. Van Buren lost the election.", "Read 1963–64; Metcalf, OK (2010)"),
  ],
  avoid=["Do not say OK came FROM 'Old Kinderhook'. The campaign spread it.",
         "Do not use the debunked origins (Choctaw 'okeh', Wolof, Greek 'ola kala')."],
  sources=["https://www.merriam-webster.com/words-at-play/the-hilarious-history-of-ok-okay", "https://www.jstor.org/stable/453290"],
  shots=[
   ("0–3", "AI clip C1 (from S1)", "A vintage hand-operated printing press with a blank newspaper sheet.", "the press lever pulls down and stamps the sheet; a puff of ink dust"),
   ("3–9", "AI still S2", "An 1830s Boston street, a newsboy in a cap holding up blank newspapers.", None),
   ("9–15", "LOCAL diagram D1", "Handwritten cards flip: O.W. = 'oll wright', K.G. = 'know go'.", None),
   ("15–22", "AI still S3", "Close-up of an old newspaper page with blank columns; we overlay 'o.k. — all correct' locally in period type.", None),
   ("22–30", "AI clip C2 (from S4)", "An 1840 election rally: top hats, a crowd, blank banners on poles.", "the crowd waves hats and the blank banners sway"),
   ("30–35", "AI still S5", "A nineteenth-century American statesman with large sideburns in a dark coat, a generic illustration rather than a portrait likeness.", None),
   ("35–40", "AI still S6", "A telegraph key with copper wires stretching away across a landscape.", None),
   ("40–47", "AI still S7", "A 1960s linguist in a library surrounded by stacks of old newspapers, holding a magnifying glass.", None),
   ("47–52", "AI still S8", "A modern hand typing on a smartphone; we overlay a chat bubble saying 'ok' locally.", None),
   ("52–55", "LOCAL end card", "Logo flip and the sign-off.", None),
  ]),
 dict(n="06", slug="windows", cat="ENGINEERING", title="Plane windows: the myth and the real story",
  yt="Why plane windows are round (it's not what you think) ✈️ #shorts",
  cover="ROUND WINDOWS? HALF TRUE", src_site="Mental Floss",
  facts=[
   ("BOAC 781 (G-ALYP) broke up off Elba on 10 Jan 1954; SAA 201 (G-ALYY) broke up near Naples on 8 Apr 1954.", "Cohen Court of Inquiry report, HMSO 1955"),
   ("The inquiry found the break-up most probably began at the corner of the rear ADF (antenna) window in the cabin roof, at a bolt hole, where fatigue was found.", "Cohen report, para 77"),
   ("Fundamental cause: stresses around the corners of windows and other cut-outs were too high for a long fatigue life.", "Cohen report, para 79"),
   ("The G-ALYU water-tank test failed at a window corner after the equivalent of about 3,060 flights (1,230 real + 1,830 tank cycles).", "Cohen report"),
   ("The Comet 1 passenger windows were rectangular with rounded corners.", "Cohen report; FAA Lessons Learned"),
  ],
  avoid=["Do not say 'square passenger windows cracked'.", "Say bolt hole, not rivet hole.", "Do not blame punch-riveting (a later, disputed claim)."],
  sources=["https://www.faa.gov/sites/faa.gov/files/2022-10/G-ALYP_Report_0.pdf", "https://www.faa.gov/lessonslearned/transport_airplane/accidents/G-ALYV"],
  shots=[
   ("0–3", "AI clip C1 (from S1)", "Close-up of a modern airliner cabin window with rounded corners, clouds outside.", "clouds drift past outside the window; light shifts gently"),
   ("3–6", "LOCAL diagram D0", "A square window shape struck through, then a question mark.", None),
   ("6–13", "AI still S2", "A 1950s de Havilland Comet jet airliner in flight, engines buried in the wing roots, sleek silver body.", None),
   ("13–22", "AI clip C2 (from S3)", "An airliner fuselage submerged in a huge indoor water tank, engineers on a gantry above.", "the water surface ripples rhythmically as if the fuselage is being pressurised and released"),
   ("22–30", "AI still S4", "Top of an aircraft fuselage with two small rectangular antenna cut-outs in the roof, an orange crack spreading from one corner.", None),
   ("30–40", "LOCAL diagram D1", "Stress lines flowing around a sharp-cornered hole (bunched up, orange) versus a rounded hole (smooth).", None),
   ("40–46", "AI still S5", "A fuselage section gently swelling and relaxing like a breathing balloon, with curved arrows.", None),
   ("46–52", "AI still S6", "Engineers with a flashlight inspecting the rounded window frames of a modern airliner.", None),
   ("52–55", "LOCAL end card", "Logo flip and the sign-off.", None),
  ]),
]

# ---------------------------------------------------------------- budget (credits; quotes from Higgsfield get_cost, 04 Nov 2026)
BUDGET = [
 ("P0", "Style lock: 2 test subjects × (GPT Image 2.5 high 1K ×2 @1.5 + Nano Banana Pro 2K ×2 @2.0)", 14.0),
 ("P0", "Motion test: same start frame on Seedance 2.0 Mini 720p 5s @5.0 and Kling 3.0 Pro 5s silent @8.75", 13.75),
 ("P0", "Voice test: Ainsley sign-off line (ElevenLabs v4, ~0.23) ×2", 0.5),
 ("P0", "Brand music bed: ElevenLabs Music v2.5, 60 s instrumental, 2 takes @8.72", 17.44),
 ("P1", "Stills: 6 eps × 8 (incl. clip start frames), priced at the dearer model (Nano Banana Pro 2K @2.0)", 96.0),
 ("P2", "Hero clips: 6 eps × 2, Seedance 2.0 Mini 720p 5s silent @5.0", 60.0),
 ("P3", "Voiceover: Ainsley, ElevenLabs v4, ~840 chars per ep ≈ 4.1 + paragraph-split overhead ≈ 5 each", 30.0),
]
CAP = 297.0  # half of 594.6

def words(t): return len(re.findall(r"[\w’'.-]+", t))

def load_script(slug, n):
    return (SCRIPTS / f"ep{n}_{slug}.txt").read_text().strip()

e = html.escape
planned = sum(b[2] for b in BUDGET)
reserve = round(CAP - planned - 10, 2)

# ---------------------------------------------------------------- REVIEW.md (compact, for the independent checker)
md = [f"# WTF Season 1 production plan (review copy)\n\nCredit cap {CAP}. Planned {planned:.2f}. Retake reserve {reserve}. Untouched safety margin 10.\n",
      f"Style block appended to every image prompt:\n> {STYLE_BLOCK}\n\nMotion block appended to every clip prompt:\n> {MOTION_BLOCK}\n",
      "## Budget"] + [f"- {p} | {d} | {c}" for p, d, c in BUDGET]
for ep in EPS:
    s = load_script(ep["slug"], ep["n"]); w = words(s) + 4
    md += [f"\n## EP{ep['n']} {ep['title']} ({ep['cat']}), {w} words, ≈{w/WPM*60:.0f}s at {WPM} wpm",
           "### Script", s + "\n" + SIGNOFF, "### Verified facts"] + [f"- {f} [{src}]" for f, src in ep["facts"]] + \
          ["### Must avoid"] + [f"- {a}" for a in ep["avoid"]] + ["### Shots"] + \
          [f"- {t}s | {kind} | {desc}" + (f" | motion: {mo}" if mo else "") for t, kind, desc, mo in ep["shots"]]
(ROOT / "REVIEW.md").write_text("\n".join(md))

# ---------------------------------------------------------------- index.html
def ep_html(ep):
    s = load_script(ep["slug"], ep["n"]); w = words(s) + 4
    paras = "".join(f"<p>{e(p)}</p>" for p in s.split("\n") if p.strip())
    stills = sum(1 for x in ep["shots"] if x[1].startswith("AI still"))
    clips = sum(1 for x in ep["shots"] if x[1].startswith("AI clip"))
    rows = "".join(
        f"<tr><td class='t'>{e(t)}s</td><td><span class='src {('ai' if k.startswith('AI') else 'loc')}'>{e(k)}</span></td>"
        f"<td>{e(d)}{('<div class=mo>Motion: ' + e(mo) + '</div>') if mo else ''}</td></tr>"
        for t, k, d, mo in ep["shots"])
    facts = "".join(f"<li>{e(f)} <span class='cite'>{e(c)}</span></li>" for f, c in ep["facts"])
    avoid = "".join(f"<li>{e(a)}</li>" for a in ep["avoid"])
    links = " · ".join(f"<a href='{e(u)}'>{e(re.sub(r'https?://(www\\.)?', '', u).split('/')[0])}</a>" for u in ep["sources"])
    return f"""
<section class="ep" id="ep{ep['n']}">
 <header class="ephead"><span class="pill">FACT {ep['n']}</span><span class="cat">{ep['cat']}</span>
  <h3>{e(ep['title'])}</h3>
  <p class="meta">{w} words · about {w/WPM*60:.0f} s at {WPM} wpm · {stills} AI stills + {clips} AI clips + local diagrams · idea source: {e(ep['src_site'])}</p></header>
 <div class="epgrid">
  <div class="script"><h4>Script (Ainsley)</h4>{paras}<p class="sign">{SIGNOFF}</p></div>
  <div class="check"><h4>Fact check: verified</h4><ul>{facts}</ul><h4>Must not say</h4><ul class="avoid">{avoid}</ul><p class="links">Sources: {links}</p></div>
 </div>
 <h4>Shot list</h4><div class="tw"><table><thead><tr><th>Time</th><th>Source</th><th>Visual (subject prompt; the style block is appended)</th></tr></thead><tbody>{rows}</tbody></table></div>
 <p class="upload"><b>Shorts/Reels title:</b> {e(ep['yt'])} &nbsp;·&nbsp; <b>Cover line:</b> {e(ep['cover'])}</p>
</section>"""

budget_rows = "".join(f"<tr><td>{p}</td><td>{e(d)}</td><td class='num'>{c:.2f}</td></tr>" for p, d, c in BUDGET)
cal = [("Thu 5 Nov", "EP01 · GPS needs Einstein", "full"), ("Fri 6 Nov", "EP04 · Not 90% bacteria", "full"),
       ("Sat 7 Nov", "Quiz cut: 'Whale's closest living relative?' (teases EP02)", "cut"), ("Sun 8 Nov", "EP02 · Whale ↔ hippo", "full"),
       ("Mon 9 Nov", "EP05 · OK was a joke", "full"), ("Tue 10 Nov", "Quiz cut: 'Why are plane windows round?' (teases EP06)", "cut"),
       ("Wed 11 Nov", "EP06 · Plane windows", "full"), ("Thu 12 Nov", "EP03 · Why 12 notes", "full"),
       ("Fri 13 Nov", "Quiz cut: '10 bacteria for every cell, true or false?'", "cut"), ("Sat 14 Nov", "Recap: 3 facts in 30 seconds", "cut")]
cal_html = "".join(f"<li class='{k}'><span class='d'>Day {i+1} · {d}</span><span>{e(t)}</span><span class='k'>{'0 credits' if k=='cut' else 'episode'}</span></li>" for i, (d, t, k) in enumerate(cal))
eps_html = "".join(ep_html(x) for x in EPS)
nav = "".join(f"<a href='#ep{x['n']}'>{x['n']}</a>" for x in EPS)

page = f"""<title>WTF Season 1 Bible</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Caveat:wght@700&family=JetBrains+Mono:wght@500;700&display=swap">
<style>
/* Layout: a single reading column styled like a night-notebook page; episodes are stacked chapters. */
:root{{--bg:#F3F5F9;--paper:#FFFFFF;--ink:#13213C;--muted:#55627A;--line:#D9DFEA;--accent:#E8730C;--accent-ink:#13213C;--chip:#FFE3C7;--ok:#1F7A4D;--bad:#B3261E;
 --display:'Bricolage Grotesque',system-ui,sans-serif;--body:'Bricolage Grotesque',system-ui,sans-serif;--hand:'Caveat',cursive;--mono:'JetBrains Mono',ui-monospace,monospace}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#0E1830;--paper:#13213C;--ink:#EEF2F8;--muted:#9AA9C4;--line:#24365E;--accent:#FF8C1A;--accent-ink:#13213C;--chip:#3A2A17;--ok:#6FD3A0;--bad:#FF8A80;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0E1830;--paper:#13213C;--ink:#EEF2F8;--muted:#9AA9C4;--line:#24365E;--accent:#FF8C1A;--accent-ink:#13213C;--chip:#3A2A17;--ok:#6FD3A0;--bad:#FF8A80;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font:500 16px/1.55 var(--body);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.wrap{{max-width:1040px;margin:0 auto;padding-block:32px 80px;display:grid;gap:40px}}
h1,h2,h3{{font-family:var(--display);font-weight:800;line-height:1.08;text-wrap:balance;margin:0}}
h1{{font-size:clamp(34px,6vw,58px);letter-spacing:-.02em}} h2{{font-size:clamp(24px,3.4vw,34px)}} h3{{font-size:clamp(20px,2.6vw,26px)}}
h4{{font:700 12px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:18px 0 8px}}
a{{color:var(--accent)}} a:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
.eyebrow{{font:700 13px var(--mono);letter-spacing:.14em;color:var(--accent);text-transform:uppercase}}
.hand{{font-family:var(--hand);font-size:28px;color:var(--accent)}}
.lede{{max-width:68ch;color:var(--muted);font-size:18px}}
.approve{{background:var(--paper);border:2px solid var(--accent);border-radius:14px;padding:20px 22px;display:grid;gap:10px}}
.approve ol{{margin:0;padding-left:20px;display:grid;gap:6px}}
.stats{{display:flex;flex-wrap:wrap;gap:12px}}
.stat{{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:12px 16px;min-width:150px;flex:1}}
.stat b{{display:block;font:800 28px var(--display);font-variant-numeric:tabular-nums}} .stat span{{font:500 13px var(--mono);color:var(--muted)}}
.tw{{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--paper)}}
table{{border-collapse:collapse;width:100%;font-size:14.5px;min-width:560px}}
th,td{{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line)}}
th{{font:700 11.5px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}}
td.num{{text-align:right;font:700 14px var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}}
td.t{{font:700 13px var(--mono);white-space:nowrap}}
tfoot td{{font-weight:800}}
.src{{font:700 11.5px var(--mono);padding:2px 8px;border-radius:6px;white-space:nowrap}}
.src.ai{{background:var(--chip);color:var(--ink)}} .src.loc{{border:1px solid var(--line);color:var(--muted)}}
.mo{{font:500 13px var(--mono);color:var(--muted);margin-top:4px}}
.kit{{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:14px}}
.kit figure{{margin:0;display:grid;gap:6px}} .kit img{{border-radius:10px;border:1px solid var(--line);display:block;width:100%;height:auto}}
.kit figcaption{{font:500 13px/1.35 var(--body);color:var(--muted)}}
.rules{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}}
.rule{{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:16px 18px;min-width:0}}
.rule ul{{margin:0;padding-left:18px;display:grid;gap:5px}}
.sw{{display:flex;gap:10px;flex-wrap:wrap}} .sw div{{flex:1;min-width:110px;border-radius:10px;padding:46px 10px 8px;font:700 12px var(--mono);border:1px solid var(--line)}}
.block{{background:var(--paper);border:1px dashed var(--line);border-radius:10px;padding:12px 14px;font:500 13.5px/1.5 var(--mono);overflow-wrap:anywhere}}
.ep{{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:22px;display:grid;gap:6px;scroll-margin-top:20px}}
.ephead{{display:grid;gap:6px}} .pill{{justify-self:start;background:var(--accent);color:var(--accent-ink);font:700 12px var(--mono);letter-spacing:.1em;padding:3px 10px;border-radius:7px}}
.cat{{font:700 12px var(--mono);letter-spacing:.14em;color:var(--muted)}} .meta{{margin:0;color:var(--muted);font-size:14px}}
.epgrid{{display:grid;grid-template-columns:1.1fr 1fr;gap:22px}} .epgrid>div{{min-width:0}}
.script p{{margin:0 0 9px;max-width:62ch}} .script .sign{{font-family:var(--hand);font-size:26px;color:var(--accent)}}
.check ul{{margin:0;padding-left:18px;display:grid;gap:6px;font-size:14.5px}} .cite{{font:500 12px var(--mono);color:var(--muted)}}
.avoid li::marker{{content:"✕  ";color:var(--bad)}} .links{{font-size:13px;color:var(--muted);overflow-wrap:anywhere}}
.upload{{font-size:14px;color:var(--muted);margin:8px 0 0}}
.cal{{list-style:none;margin:0;padding:0;display:grid;gap:8px}}
.cal li{{display:grid;grid-template-columns:170px 1fr auto;gap:12px;align-items:center;background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:10px 14px}}
.cal li.full{{border-left:5px solid var(--accent)}} .cal .d{{font:700 13px var(--mono)}} .cal .k{{font:500 12px var(--mono);color:var(--muted)}}
nav.jump{{display:flex;gap:8px;flex-wrap:wrap;align-items:center}} nav.jump a{{font:700 13px var(--mono);text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:4px 10px;background:var(--paper)}}
@media (max-width:760px){{.epgrid{{grid-template-columns:1fr}} .cal li{{grid-template-columns:1fr}} }}
</style>
<div class="wrap">
<header style="display:grid;gap:14px">
 <span class="eyebrow">Wait, That's a Fact? · Season 1 · production bible v1</span>
 <h1>Six facts, one look, 297 credits</h1>
 <p class="lede">The plan for six Shorts and Reels under 60 seconds, plus four extra posts cut from the same footage at no credit cost, covering ten days. Every script is fact-checked. Each asset is designed once and reused. Every generation is priced before it runs. Nothing has been rendered yet.</p>
 <nav class="jump"><span class="cat">Jump to episode</span>{nav}<a href="#budget">budget</a><a href="#calendar">calendar</a></nav>
</header>

<section class="approve" aria-labelledby="ap"><h2 id="ap">What happens when you approve</h2>
<ol>
 <li><b>P0 · Lock the look (≈46 cr).</b> I generate two style-test subjects on two image models, one motion test on two video models, the Ainsley sign-off line and two music-bed takes. I pick the winning image model and video model by a fixed checklist (style match, clean lines, no stray text, palette).</li>
 <li><b>P1 · Stills (≤96 cr).</b> 48 illustrations generated in batches. Each carries the same style block and the two locked style frames as references. Any still that fails the checklist is redone from the retake reserve.</li>
 <li><b>P2 · Hero clips (≈60 cr).</b> Two 5-second image-to-video clips per episode, made from approved stills only.</li>
 <li><b>P3 · Voice (≈30 cr).</b> Ainsley reads each script in paragraphs, so one fluffed line costs one paragraph to fix, not the whole take.</li>
 <li><b>P4 · Edit (0 cr).</b> I build all diagrams, captions, the grid overlay, sound design and end cards here with ffmpeg and the brand kit. Then I deliver six 1080×1920 masters and four quiz or recap cuts.</li>
</ol>
<p style="margin:0"><b>Hard rule:</b> I never pass {CAP:.0f} credits, which is half of your 594.6. Before every job I price it with Higgsfield's free cost check and keep a running ledger. If the retake reserve runs out, I stop and ask.</p>
</section>

<section id="budget" style="display:grid;gap:14px"><h2>Credit budget</h2>
 <div class="stats">
  <div class="stat"><b>{CAP:.1f}</b><span>hard cap (half of 594.6)</span></div>
  <div class="stat"><b>{planned:.1f}</b><span>planned spend</span></div>
  <div class="stat"><b>{reserve:.1f}</b><span>retake reserve</span></div>
  <div class="stat"><b>10.0</b><span>never touched</span></div>
 </div>
 <div class="tw"><table><thead><tr><th>Phase</th><th>Line item</th><th>Credits</th></tr></thead><tbody>{budget_rows}</tbody>
 <tfoot><tr><td></td><td>Planned total</td><td class="num">{planned:.2f}</td></tr></tfoot></table></div>
 <p class="lede" style="font-size:15px">These prices are Higgsfield's own quotes from today, 4 Nov 2026. If Kling 3.0 Pro wins the motion test (8.75 per clip), I make 10 clips instead of 12, which keeps the total about the same. Nothing is spent on what costs nothing: diagrams, numbers, captions, covers, logo, end cards and the four quiz or recap cuts are built locally. AI models still get numbers and text wrong, so no number ever appears in a generated image.</p>
</section>

<section style="display:grid;gap:14px"><h2>Model choices</h2>
 <div class="rules">
  <div class="rule"><h4>Images</h4><ul><li><b>Nano Banana Pro 2K</b> (2 cr) vs <b>GPT Image 2.5 high</b> (1.5 cr), decided by the P0 test. Both take reference images, which is what keeps 48 stills looking like one series.</li><li>Rejected: FLUX 3 (dearer for the same job), Soul (built for photoreal people).</li></ul></div>
  <div class="rule"><h4>Video</h4><ul><li><b>Seedance 2.0 Mini 720p</b> (5 cr per 5 s, silent). It accepts start and end frames plus style references.</li><li><b>Kling 3.0 Pro</b> (8.75 cr) is the challenger in the P0 test.</li><li>Rejected: Seedance 2.5 (35 cr), Veo, MiniMax H3 (12.5). The extra quality doesn't show on flat 2D art.</li></ul></div>
  <div class="rule"><h4>Voice and music</h4><ul><li><b>Ainsley</b> on <b>ElevenLabs v4</b>, the voice you chose for the pilot. About 0.5 cr per 100 characters.</li><li>One brand music bed (ElevenLabs Music v2.5) reused in every episode as the channel's sound.</li><li>Ainsley's sign-off line is recorded once and reused in every episode.</li></ul></div>
 </div>
</section>

<section style="display:grid;gap:14px"><h2>Brand kit and mockups</h2>
 <p class="lede" style="font-size:15px">These are built and ready now. The illustrations in the mockups are placeholders I drew to show layout, type and colour. The final art comes from the P0 style lock.</p>
 <div class="kit">
  <figure><img src="mockups/logo.png" alt="Logo: an orange question mark whose lower stem and dot are a white exclamation mark"><figcaption><b>Logo.</b> At a glance it's a "?". Look again and the white "!" is hidden inside it. Wait… that's a fact.</figcaption></figure>
  <figure><img src="mockups/hook.jpg" alt="Hook frame mockup for episode 1"><figcaption><b>Hook frame.</b> FACT badge top left, caption block in the safe zone, key word on an orange block.</figcaption></figure>
  <figure><img src="mockups/diagram.jpg" alt="Diagram frame mockup with +45, −7 and +38 microsecond bars"><figcaption><b>Diagram frame.</b> Built locally so every number is exact. The source tag shows the reference on screen.</figcaption></figure>
  <figure><img src="mockups/safe.jpg" alt="Caption style with safe zones marked"><figcaption><b>Captions and safe zones.</b> The red boxes are where the Shorts and Reels buttons and title sit. Nothing important goes there.</figcaption></figure>
  <figure><img src="mockups/cover.jpg" alt="Cover mockup for episode 2"><figcaption><b>Cover.</b> 3 to 5 words, one in orange, the badge, and a single hero illustration.</figcaption></figure>
  <figure><img src="mockups/endcard.jpg" alt="End card with logo and sign-off"><figcaption><b>End card (2 s).</b> The orange hook lifts away and leaves the "!". Same audio line every time.</figcaption></figure>
  <figure><img src="mockups/bg.jpg" alt="Navy grid notebook background plate"><figcaption><b>Notebook overlay.</b> Grid, orange margin line and chalk grain sit on top of every shot, AI or local, so all six episodes feel like one notebook.</figcaption></figure>
 </div>
 <div class="sw">
  <div style="background:#13213C;color:#fff">NAVY #13213C</div><div style="background:#FF8C1A;color:#13213C">ORANGE #FF8C1A</div>
  <div style="background:#FFFFFF;color:#13213C">WHITE #FFFFFF</div><div style="background:#DCE6F2;color:#13213C">CHALK #DCE6F2</div><div style="background:#6F84A8;color:#fff">SLATE #6F84A8</div>
 </div>
</section>

<section style="display:grid;gap:14px"><h2>Style bible</h2>
 <div class="rules">
  <div class="rule"><h4>Narrative</h4><ul><li>Every episode follows the same arc: <b>surprising claim → why it seems wrong → mechanism → reframe → "Wait… that's a fact."</b></li><li>The first sentence is the hook and is on screen by 0.5 s.</li><li>The tone is clear, plain and slightly cheeky. Nothing is overclaimed: "about", "roughly" and "more than" wherever the source is approximate.</li><li>Every episode is 135–150 words including the sign-off, about 52–58 s.</li></ul></div>
  <div class="rule"><h4>Edit grammar</h4><ul><li>The visual changes at least every 2–4 s, and the first change comes by 1.5 s.</li><li>Stills get a slow 3–6% push-in or a two-layer parallax. Diagrams draw on in chalk strokes.</li><li>Cuts are hard cuts. There is one signature orange marker-swipe, at the hook→mechanism turn.</li><li>The badge (FACT 0X · TOPIC) stays on screen throughout. A source tag appears on every number.</li></ul></div>
  <div class="rule"><h4>Captions</h4><ul><li>Bricolage Grotesque ExtraBold, uppercase, 88–96 px, 1–3 words per chunk.</li><li>The key word in each chunk sits on an orange block. Numbers are set in JetBrains Mono.</li><li>Captions sit between y≈1150 and 1400 px and stay clear of the bottom 420 px and the right 150 px, which is the Shorts and Reels UI.</li></ul></div>
  <div class="rule"><h4>Sound</h4><ul><li>Ainsley's VO is normalised. The final mix is −14 LUFS integrated with a −1 dBTP ceiling, so YouTube and Instagram won't turn it down.</li><li>The brand bed runs about 20 dB under the VO and is ducked under speech.</li><li>Chalk-scribble SFX play on draw-ons. A single soft "ding" plays on the reveal line.</li></ul></div>
  <div class="rule"><h4>Consistency checks (every shot)</h4><ul><li>Navy background, palette only.</li><li>White chalk outline, same line weight.</li><li>No text or numbers inside the art.</li><li>Subject is centred, with the top 15% and bottom 30% clear.</li><li>Recurring props are drawn the same way every time: the satellite in EP01, the human silhouette in EP04.</li><li>Any shot that fails one check is regenerated.</li></ul></div>
  <div class="rule"><h4>Delivery spec</h4><ul><li>1080×1920, 30 fps, H.264 High at about 14 Mbps, AAC 48 kHz at 320 kbps.</li><li>Captions are burned in.</li><li>Same master for YouTube Shorts and Instagram Reels.</li><li>Upload a separate cover image for each.</li><li>Turn on the AI-content label on Instagram. On YouTube, the disclosure isn't required for clearly animated content, but I'd tick it anyway for trust.</li></ul></div>
 </div>
 <h4>Style block (appended to every image prompt)</h4><div class="block">{e(STYLE_BLOCK)}</div>
 <h4>Motion block (appended to every clip prompt)</h4><div class="block">{e(MOTION_BLOCK)}</div>
</section>

<section style="display:grid;gap:18px"><h2>The six episodes</h2><span class="hand">scripts, fact checks and shot lists</span>{eps_html}</section>

<section id="calendar" style="display:grid;gap:14px"><h2>Ten-day calendar</h2>
 <p class="lede" style="font-size:15px">Post the same video to YouTube Shorts and Instagram Reels on the same day, around 7 pm IST, until your analytics suggest a better time. The four cut days reuse existing footage: a 10–15 s quiz that teases the next episode, and a recap. They cost nothing.</p>
 <ul class="cal">{cal_html}</ul>
</section>

<section style="display:grid;gap:10px"><h2>Risks I'm managing</h2>
 <div class="rules">
  <div class="rule"><ul><li><b>Style drift across 48 stills.</b> Fixed style block, the same two reference frames on every call, and the shared notebook overlay.</li><li><b>Text or numbers appearing in AI art.</b> Forbidden in the prompt and checked on every image. All type is added in the edit.</li></ul></div>
  <div class="rule"><ul><li><b>Running long.</b> The scripts are timed at 155 wpm. If Ainsley reads slower, I speed up the take by up to 4% without changing pitch; beyond that I trim a line before re-recording.</li><li><b>Credits.</b> Each job is priced before it runs, the ledger is kept as I go, and the work stops at {CAP:.0f}.</li></ul></div>
 </div>
</section>
</div>"""
(ROOT / "index.html").write_text(page)
print("planned", planned, "reserve", reserve)
for ep in EPS:
    s = load_script(ep["slug"], ep["n"]); print(ep["n"], words(s) + 4)
