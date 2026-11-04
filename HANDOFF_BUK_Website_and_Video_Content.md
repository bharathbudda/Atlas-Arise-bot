# Handoff: BUK Law Partners website and animated video content

**Written:** 4 November 2026, at the end of the session that rebuilt buklawpartners.com.
**For:** the next Claude session, which will produce the animated short-form video series and keep extending the website.
**Owner:** Bharath Budda (Founding Partner, BUK Law Partners).

> This repository is **public**. This file deliberately leaves out private photo links and account identifiers. Keep it that way: never commit client details, credentials, or personal photos here.

---

## 0. Read this first

1. **Website:** live at https://buklawpartners.com, published by Netlify from the `buklawpartners-site/` folder on `main`. Anything merged to `main` goes live within about 30 seconds. Work on a branch and check the Netlify branch preview first (section 3.3).
2. **Video series:** the plan is in section 6, with a fully written sample script in section 6.9. Nothing has been produced yet: no scripts beyond the sample, no assets, no channels set up.
3. **Every piece of content must pass two checks before it is published:**
   - **Bar Council of India Rule 36** (no solicitation or self-praise). The rules are in section 4.
   - **Legal accuracy.** Bharath's standing instruction: whenever he says "double check", spawn an **independent agent** to look for inaccuracies, mistakes and logical flaws, keeping its prompt short to save tokens. On this site that check already caught 14 problems (section 5), so treat it as mandatory for every script and article.
4. **Open questions for Bharath** are in section 8. Ask them at the start rather than guessing.

---

## 1. The firm

| Item | Detail |
|---|---|
| Name | BUK Law Partners, "Advocates & Legal Consultants" |
| Office | Flat No. 103, VV Plaza, RR Colony, Tirupati, Andhra Pradesh 517 501 |
| Phone / WhatsApp | +91 7337079411 |
| Email | buklawoffice@gmail.com |
| Since | 1995 (Budda Udaya Kumar enrolled in 1995) |
| Forums | High Court of AP (Amaravati); DRT Hyderabad (and DRAT); district and subordinate courts in Tirupati and Chittoor; NCLT Amaravati Bench; revenue authorities (RDO, MRO, Joint Collector); arbitral tribunals |
| Areas | Property and land, title disputes, revenue matters, writs (Art. 226), civil suits and appeals, DRT/SARFAESI, land acquisition, commercial and IBC, family and succession, legal opinions and due diligence, agreements and leases, bail and criminal, consumer, startup counsel |

### People (as shown on the website)

| Name | Role on site | Photo on site |
|---|---|---|
| Budda Udaya Kumar | Founding & Senior Partner, in practice since 1995 | AI-generated portrait made from his own photos (seated in the teal library chair, navy suit). Bharath chose it and approved the deploy. |
| Bharath Budda | Founding Partner & Advocate, High Court of A.P. Enrolment AP/2224/2018. BA LLB (Hons.) JGU 2012–17; LLM (Distinction) QMUL 2017–18; MSc Social Innovation & Entrepreneurship, LSE 2022–23. Formerly Associate (Strategic Initiatives), Spice Route Legal; co-founder, LegalE Innovation Pvt. Ltd.; legal analyst, Solomonic. | His real photo (teal library chair) |
| A. Venkatesulu | Senior Associate, 20+ years | Real photo |
| T. Kiran Kumar | Senior Associate, 10+ years | **Missing**: shows initials |
| K. Pramod Kumar Reddy | Associate, 2+ years | **Missing**: shows initials |
| Suda Tejaswi Sreenivas | Associate, 2+ years | Real photo |
| Majjiga Venkat Sai | Associate, 2+ years | Real photo |
| T. Muni Sekhar | Associate, 2+ years | Real photo |
| A. Yaswanth Kumar Reddy | Associate, 1 year | Real photo |

These spellings were confirmed by Bharath; use them exactly.

### About Bharath (how to work with him)

- He is a litigation lawyer in Andhra Pradesh and a legal-tech founder. He thinks in systems and wants repeatable frameworks.
- He prefers plain, structured answers and a clear recommendation rather than a list of options.
- **Standing rule:** "double check" means spawn an independent agent to check the final output, with a token-efficient prompt.
- He gives quick approvals ("looks okay, deploy"), so make previews easy to check.
- The firm has drafting skills in this environment (`buk-pleading-style`, `buk-legal-notice`, `buk-legal-research`, `buk-title-opinion`, etc.). Use `buk-legal-research` when checking the law behind a script.

---

## 2. What was done in this session (chronological)

1. **Reviewed the live site.** Good design and SEO groundwork, but it had Rule 36 problems, a placeholder Google Analytics ID (`G-XXXXXXXXXX`) so no data had ever been collected, 404s on all 9 team photos, two disclaimer pop-ups, legal errors, and comma splices left behind by an earlier bulk "em dash to comma" find-and-replace.
2. **Found that Bharath's local files were older than the live site.** The June 2025 uploads had 10 pages; the live site had 24. The repo was seeded from the live site, plus five original source files Bharath uploaded later.
3. **Put the site in this repo** under `buklawpartners-site/`, separate from the Atlas Telegram bot in the repo root, which is unrelated and runs on Railway.
4. **Connected Netlify** to this repo, with branch deploys turned on.
5. **Fix pass** (PR [bharathbudda/Atlas-Arise-bot#1](https://github.com/bharathbudda/Atlas-Arise-bot/pull/1), merged and deployed):
   - neutral wording on 18 pages; neutral page titles and meta descriptions; FAQ structured data removed;
   - "Senior Advocate" removed (section 4.3);
   - GA4 `G-EC6HXDFYV4` on every page;
   - the disclaimer pop-up moved into shared `assets/`, and the second bar removed;
   - portrait partner cards and associate photos;
   - the enquiry form now reports failed submissions, and the Netlify form marker was restored;
   - new `privacy.html` (DPDP Act); favicon; sitemap updated;
   - legal corrections, followed by the independent review (section 5).
6. **Verified after deploy:** all 25 pages return 200, no console errors, the pop-up behaves correctly, no horizontal scroll on mobile, the form is detected by Netlify, and GA is present.

---

## 3. Website: technical reference

### 3.1 Hosting and deployment

- **Netlify** project `buklawpartners` (team "BUk Law Partners"), linked to `bharathbudda/Atlas-Arise-bot`.
- Production branch `main`; base directory `buklawpartners-site`; no build command. `buklawpartners-site/netlify.toml` sets the publish directory to `.` and adds security headers.
- **Branch deploys** are on for `claude/busy-bohr-p4iavr`. Preview URL: `https://claude-busy-bohr-p4iavr--buklawpartners.netlify.app`. Other branch names give `https://<branch-with-slashes-as-dashes>--buklawpartners.netlify.app`, but only if that branch is added under *Project configuration → Build & deploy → Branches and deploy contexts → Branch deploys*. Alternatively, open a PR and Netlify builds a Deploy Preview.
- **Go live:** PR into `main`, then merge. Only merge after Bharath approves the preview.
- **Forms:** Netlify Forms, form name `consultation`. The source `<form>` must keep `data-netlify='true' netlify-honeypot='bot-field'`; Netlify strips these from the deployed HTML, which is normal. Bharath was asked to send one test enquiry and turn on email notifications. Check with him whether he has.
- **Analytics:** GA4 Measurement ID `G-EC6HXDFYV4` (public, not a secret). The tag sits right after the viewport meta tag on every page. The homepage also fires `gtag('event','consultation_request')` when the form is submitted.
- **Search Console:** Bharath was asked to submit `https://buklawpartners.com/sitemap.xml`. Not confirmed.

### 3.2 How the pages are built

- Plain static HTML. Each page has its own inline `<style>` with the same design tokens. There is no build system.
- Shared files: `assets/disclaimer.css` and `assets/disclaimer.js` (the entry pop-up; acceptance is stored in `sessionStorage` under `bukDisclaimerAccepted`), plus `favicon.svg` and `favicon.ico`.
- Each page still contains the pop-up's HTML markup inline (`#entryDisclaimer`); only its CSS and JS are shared.
- Links: the original source pages use `x.html`. Pages taken from the live snapshot use clean `/x` links, which Netlify rewrote. Both work. Canonical tags and the sitemap use `https://buklawpartners.com/x.html`.
- **New page checklist:**
  - copy an existing page of the same type (service page: `buying-land-tirupati.html`; article: `insight-encumbrance-certificate.html`);
  - keep the GA tag, favicon links, disclaimer markup, `assets/disclaimer.css/js`, and the footer "Privacy notice" link;
  - set the title, description, canonical and og tags;
  - add the page to `sitemap.xml`, to `insights.html` (for articles), and to related-links blocks;
  - do not add FAQPage structured data.
- **Design tokens:**
  - navy `#0C2D5A`, steel `#1B3A5C`, steel-mid `#2E5F8A`;
  - gold `#C9A84C`, gold-light `#E8D5A3`, parchment `#F5F0E8`, ivory `#F7F4EE`;
  - ink `#0E1C2E`, text-mid `#3A4A5C`;
  - fonts: Cormorant Garamond (headings), DM Sans (body), JetBrains Mono (labels and tags);
  - motif: gold scales of justice; fine diagonal gold hairlines on navy;
  - tagline: "Principled Advocacy. Rooted in Research."

### 3.3 Page inventory (all live)

| Type | Pages |
|---|---|
| Home | `index.html` (sections: hero, about, practice areas, how we work, people, courts, startup counsel, insights, contact modal) |
| Service pages | `property-lawyer-tirupati`, `property-revenue-disputes-tirupati`, `buying-a-flat-tirupati`, `buying-land-tirupati`, `land-acquisition-lawyer-tirupati`, `civil-disputes-lawyer-tirupati`, `debt-recovery-sarfaesi-lawyer-ap`, `consumer-lawyer-tirupati`, `high-court-lawyer-tirupati`, `writ-petition-lawyer-ap`, `bail-criminal-lawyer-tirupati`, `agreements-contracts-lawyer-ap`, `lease-agreement-lawyer-tirupati`, `will-drafting-succession-ap` |
| Articles | `insights.html` (index); `insight-documents-before-buying-land`, `insight-22a-register-explained`, `insight-buffer-zone-water-bodies`, `insight-revenue-records-explained`, `insight-flat-buyer-mistakes`, `insight-land-buyer-mistakes`, `insight-encumbrance-certificate`, `article-title-disputes-ap` |
| Other | `privacy.html`, `robots.txt`, `sitemap.xml` (25 URLs), `og-image.png` |

### 3.4 Website backlog (not done)

1. **Comma-splice sweep** across all pages. The earlier "em dash to comma" replacement created run-on sentences, e.g. "does not require you to be in the same city, we assist". Fix by reading each page and correcting by hand. Do **not** use a bulk find-and-replace: that is what caused the problem.
2. Replace the **emoji icons** on the homepage (practice cards, about pillars, startup cards) with simple gold line SVG icons.
3. **District naming:** the site says "Chittoor District" in many places. Since the April 2022 reorganisation, Tirupati and most of the listed towns are in **Tirupati district**. Bharath has not yet decided the wording; ask him (e.g. "Tirupati and Chittoor districts").
4. Photos for T. Kiran Kumar and K. Pramod Kumar Reddy. When they arrive, save them as `photos/kiran-kumar.jpg` and `photos/pramod-kumar.jpg` and restore the `<img>` tags in `index.html`; the initials circles are currently shown directly.
5. **Homepage figures** ("HC / High Court AP", "AP / State-wide") are weak; consider replacing them.
6. **More pages for search** (Bharath wants more pages and topics). Each should pair with a video (section 6). Candidates:
   - cheque bounce (s.138 NI Act);
   - partition suits;
   - legal heir vs succession certificate in AP;
   - registering rental agreements;
   - filing a consumer complaint (forum by value, section 5);
   - RERA complaints in AP;
   - mutation and passbook correction;
   - land grabbing (AP Land Grabbing (Prohibition) Act);
   - anticipatory bail explained (BNSS);
   - GPA sales (Suraj Lamp).
7. `insights.html` and the homepage "Legal Insights" block need updating whenever an article is added.

---

## 4. Compliance guardrails (apply to the site and every video)

### 4.1 BCI Rule 36

The 2008 amendment allows a website to show only factual information: name, address, contact details, enrolment, qualifications, and areas of practice. Treat social media at least as strictly; there is no clear safe harbour for promotional reels.

**Never use:**
- self-praise: "expert", "best", "leading", "trusted", "mastery", "rare", "decisive advantage", "strongest";
- guarantees: "we ensure", "protects you", "safe to buy" stated as a promise, "buy with confidence";
- urgency or solicitation: "call us now", "act quickly", "don't wait", "book a consultation", "DM us", "link in bio for a consultation";
- testimonials, client names, case wins, success rates, fees as an offer;
- "Senior Advocate" for anyone not designated under s.16(2) Advocates Act (section 4.3).

**Allowed:**
- neutral information; explaining the law; "for enquiries about this area of the firm's practice, you are welcome to contact the office";
- the firm's name, address and website as identification.

Rewrite pattern used on the site: "BUK Law Partners provides prompt, capable representation" became "The firm's advocates appear at every stage of a criminal proceeding".

### 4.2 Disclaimers

- The website has a full-screen entry pop-up (BCI wording) and footer disclaimers.
- Every video ends with an on-screen line: **"General information, not legal advice. BUK Law Partners, Advocates, Tirupati."** Put a fuller version in the caption.

### 4.3 The "Senior Advocate" decision

Bharath used "Senior Advocate" informally to mean a senior, experienced practitioner. It was replaced because the title is a statutory designation and readers take it in that sense. The agreed wording is **"Founding & Senior Partner · In practice since 1995"**. Use the same wording in videos (e.g. on an end card); never "Senior Advocate".

### 4.4 Privacy

- `privacy.html` covers: the enquiry form fields, Google Analytics cookies, Netlify and Google as processors (possibly outside India), retention, a request not to send confidential details through the form, and DPDP Act rights. Contact: buklawoffice@gmail.com.
- Bharath was asked to review it as a lawyer.
- If a video campaign collects anything (comments, lead forms), keep it out of scope or update the notice first.

---

## 5. Legal positions already verified (reuse in scripts)

The independent review agent checked these in this session. Where it marked a point medium confidence, the content says "verify on current records".

| Topic | Position used on the site |
|---|---|
| 30-year presumption | s.92 Bharatiya Sakshya Adhiniyam 2023 (formerly s.90 Evidence Act). The court **may** presume signature, handwriting, execution and attestation. It does not prove the truth of the contents or the title, and does not apply to certified copies (*Lakhi Baruah*, 1996). |
| GPA sales | *Suraj Lamp & Industries v State of Haryana* (2012) 1 SCC 656: SA/GPA/will transactions are not transfers; title passes only by a registered conveyance. A registered sale deed executed by a GPA holder under a valid, subsisting power **does** pass title. |
| Intestate succession example | Heirs inherit by law (HSA s.8); no succession certificate or probate is needed for land. A son selling alone conveys at most his undivided share; the other Class I heirs (widow, daughters, sons) can challenge. Proof: death certificate, family member or legal heir certificate. A succession certificate covers only debts and securities. |
| Undischarged mortgage | Without a registered release or other proof of discharge, treat the mortgage as subsisting. If outstanding, it binds later purchasers. Enforceability also depends on limitation (Arts. 62/63). Equitable mortgages may not appear on the EC. |
| Adangal vs ROR 1-B | Separate registers; read them together. Revenue records are evidence of possession and fiscal liability, **not proof of title**. The pattadar passbook is evidence, not conclusive proof. |
| EC | Shows registered transactions only, not validity or adverse possession. Red flag: a person sells, then later mortgages the same land. |
| Assigned land (AP) | Transfer in breach of the AP Assigned Lands (POT) Act 1977 is void. A 2023 amendment relaxed the bar for older assignments; registrations of such "freehold" land were frozen in 2024 pending review and are being released in stages. **Medium confidence (news sources): verify current GOs before scripting.** |
| Endowment land | Can be alienated with sanction (s.80 AP Endowments Act 1987). |
| Buyer of void land | Usually loses the land but keeps a money claim against the seller (TPA s.55(2); Contract Act s.65), which may be hard to recover. Do not say "lose everything with no remedy". |
| Agricultural land conversion | AP changed its conversion regime in 2025; approvals and fees moved to local bodies and development authorities. Sources disagree on which Act was repealed. **Medium confidence: verify before scripting.** |
| s.22A Registration Act (AP) | AP State amendment; prohibited list (government, assigned, endowment, wakf, local-body, ceiling-surplus and other notified land). A private title dispute is **not** a ground for listing (Full Bench, *Vinjamuri Rajagopala Chary*). |
| Agreement of sale (AP) | Compulsorily registrable under the AP amendment to s.17(1) (AP Act 4 of 1999), whether or not possession is delivered. With possession, stamp duty is as on a sale. Agreements on or after 24 Sept 2001 must be registered for s.53A protection (s.17(1A)). An unregistered agreement is still evidence in a specific performance suit (proviso to s.49). |
| RERA | Real Estate (Regulation and Development) Act 2016; most projects must register before marketing. |
| Bail | Anticipatory bail: s.482 BNSS (formerly s.438 CrPC), to the Court of Session or High Court, by a person apprehending arrest for a non-bailable offence. Quashing: inherent powers, s.528 BNSS (formerly s.482 CrPC). |
| Land acquisition | 2013 Act. Reference to the LARR Authority under s.64 (civil court under s.18 only for acquisitions still under the 1894 Act). Withdrawal under s.93 before possession. Lapse under s.24(2) as explained in *Indore Development Authority v Manoharlal* (2020). |
| Consumer forum | Pecuniary jurisdiction by **value of consideration paid** (CPA 2019; 2021 rules): District up to Rs 50 lakh; State above Rs 50 lakh to Rs 2 crore; National above Rs 2 crore. |
| Article 300-A | Constitutional right, not a fundamental right. |
| Company / IBC | NCLT and NCLAT; the High Court keeps only legacy winding-up matters. |
| DRT | Chittoor-area matters go to DRT Hyderabad (DRT-2); appeals to DRAT. |

---

## 6. Animated video series: plan

### 6.1 Concept

Bharath wants fully animated, narrated explainer videos in the style of "What A Fact?": no presenter on camera; a voiceover tells a short story while animation, icons and kinetic text explain each fact.

- **Do not copy that channel's characters, logo, music, intro or look.** Use the genre (narrated 2D motion-graphics explainers) with BUK's own visual identity.
- Confirm with Bharath which specific episodes he likes and why (pace, humour, art style), and record the answer here.

**Purpose:** public legal education that builds recognition for the firm, sends people to the website's guides (more pages, better search ranking), and stays within Rule 36. Every video is an explainer, never an advert.

### 6.2 Proposed series identity (for Bharath to confirm)

- Working series name: **"Know Before You Sign"**. Alternatives: "Law in 60 Seconds", "BUK Explains", "Bhoomi Basics" (for the land series).
- Recurring sign-off line: *"Know the law before you sign."*
- Channels: YouTube Shorts, Instagram Reels, Facebook Reels. Later, longer YouTube cuts (4–6 minutes) that join 3–5 shorts from one topic group.

### 6.3 Format

- **9:16 vertical, 1080×1920, 45–60 seconds** for the first batch (keep it under 60s for reach and attention).
- **Language:** Bharath has not decided yet (section 8). Recommended: produce in **Telugu with English subtitles** plus an English version; Tirupati audiences reach far more in Telugu. Every Telugu script needs a human (Bharath or an associate) to check the legal terms.
- **Voice:** one consistent narrator voice per language: calm, warm, authoritative, not salesy. AI voice is fine if natural; record a human voice if the AI's Telugu sounds unnatural.
- **Captions:** burned in, high contrast, 2 lines maximum, with key terms highlighted in gold.
- **Music:** light, neutral, royalty-free; lower it under the voiceover.

### 6.4 Visual design system (matches the website)

- **Palette:** navy `#0C2D5A` background, gold `#C9A84C` accents, parchment `#F5F0E8` for document and paper surfaces, steel blue for secondary shapes. Red only for warning stamps.
- **Type:** Cormorant Garamond for titles; DM Sans for captions; JetBrains Mono for labels such as "STEP 1" and "SECTION 22A".
- **Style:** flat 2D vector, clean lines, gentle motion. Documents animate in as parchment cards with gold borders; "red flag" stamps hit with a soft thud; checklists tick in gold.
- **Recurring characters** (original, for continuity):
  - **Ravi & Lakshmi**: a Tirupati couple buying their first flat or plot (the buyer's view);
  - **Ammamma (grandmother)**: inheritance and family property episodes;
  - **a small gold scales-of-justice mascot** that "points" at the key document. Optional; check Bharath likes it.
- **Recurring locations:** a Tirupati street, a Sub-Registrar office counter, a village revenue office, a building site, a family living room. No real people, logos or real project names.
- **End card (same every time):** navy, gold scales logo, "BUK Law Partners · Advocates · Tirupati · buklawpartners.com", plus the disclaimer line.

### 6.5 Script structure (every episode)

| Time | Part | Content |
|---|---|---|
| 0–3s | **Hook** | A question or surprising fact, on screen and in voiceover ("Before you pay for a flat, ask for these 4 documents.") |
| 3–12s | **Story set-up** | A character in a relatable moment (signing, paying, inheriting) |
| 12–45s | **The facts** | 3–5 numbered points, one visual each, plain language, one legal reference at most |
| 45–53s | **Recap** | All points on one card |
| 53–60s | **Sign-off** | "Full guide on buklawpartners.com" + series line + disclaimer |

Script rules:
- Short sentences, about 130–150 words for 60s in English (Telugu runs longer; keep the facts, cut the extras).
- No jargon without a one-line meaning.
- Every legal statement must match section 5 or a verified website page.

### 6.6 CTA policy (Rule 36 safe)

- **Allowed:**
  - "The full checklist is on buklawpartners.com" (or the specific guide's URL in the caption);
  - "Follow for part 2";
  - "Save this before you buy".
- **Not allowed:**
  - "Call us", "DM us", "Book a consultation", "Link in bio to contact a lawyer";
  - phone numbers in the video;
  - "We can help you";
  - before/after case stories.
- **Caption template:** a one-line summary + 3–5 bullet facts + "Full guide: https://buklawpartners.com/<page>" + "General information, not legal advice. BUK Law Partners, Advocates, Tirupati." + a few hashtags (e.g. #Tirupati #AndhraPradesh #PropertyLaw #RERA #LandRecords). Do not use "#lawyer #bestlawyer"-style tags that read as advertising.

### 6.7 Episode plan (first batch: buying a flat and buying land)

Each episode links to an existing page, which is its fact source and the landing page in its caption.

**Group A: Buying a flat** (sources: `buying-a-flat-tirupati.html`, `insight-flat-buyer-mistakes.html`, `insight-encumbrance-certificate.html`)

| # | Title | Core points |
|---|---|---|
| A1 | Is this flat safe to buy? 4 documents to ask for | land title + EC; RERA registration; building approvals; builder agreement. *(full script in 6.9)* |
| A2 | "The builder says everything is clear" | the builder is the seller; independent check; what builders may not volunteer |
| A3 | RERA in 60 seconds | what registration discloses (promoter, approvals, timelines); why unregistered projects are a risk |
| A4 | The builder agreement trap | one-sided clauses, hidden charges, delivery and delay terms; read before signing |
| A5–A6 | 8 mistakes flat buyers make (parts 1 and 2) | from the insight article |
| A7 | What an EC shows, and what it hides | registered transactions only; not validity or possession |

**Group B: Buying land** (sources: `buying-land-tirupati.html`, `insight-documents-before-buying-land.html`, `insight-22a-register-explained.html`, `insight-buffer-zone-water-bodies.html`, `insight-revenue-records-explained.html`, `insight-land-buyer-mistakes.html`, `article-title-disputes-ap.html`)

| # | Title | Core points |
|---|---|---|
| B1 | 7 documents before you buy land in AP | title deed and link documents, EC, patta/passbook, adangal, FMB, 22A check, land-use status |
| B2 | What is the 22A list? | prohibited categories; how to check; a private dispute alone is not a ground |
| B3 | The assigned-land trap | assigned and endowment land; void transfers; 2023 relaxation and 2024 freeze (**verify current status first**) |
| B4 | Buying near a lake or tank? Buffer zones | from the buffer-zone article |
| B5 | Adangal, patta, FMB: what each one proves | revenue records ≠ title; read together with deeds |
| B6 | The "GPA sale" mistake | SA/GPA/will ≠ sale (*Suraj Lamp*); registered sale deed by a GPA holder is different |
| B7 | One heir sold the whole land | Class I heirs; undivided share; proof of heirship |
| B8 | Can you build on agricultural land? | 2025 change, local-body approval and fee (**verify first**) |

**Later groups** (each needs a new website page first or alongside):
- C: inheritance and wills (will vs intestacy, legal heir vs succession certificate, registering a will, partition);
- D: agreements and rentals (agreement-of-sale registration in AP, lease vs leave-and-licence, rental agreement basics);
- E: everyday disputes (cheque bounce s.138, consumer complaint forum by value, land grabbing, injunction basics);
- F: criminal basics (anticipatory vs regular bail under the BNSS, what an FIR is, quashing). Keep these strictly informational; they carry the highest solicitation risk.

### 6.8 Production pipeline

1. **Script (EN):** use the structure in 6.5 and facts from section 5 or the source page.
2. **Independent legal check:** a separate agent with a short prompt, listing problems only.
3. **Compliance check** against 4.1 and 6.6.
4. **Telugu adaptation**, checked by Bharath or an associate for legal terms (*pattadar*, *adangal*, *vaarasulu*, etc.).
5. **Storyboard:** one frame per beat, with the on-screen text written out.
6. **Assets:** characters and backgrounds in the 6.4 style. The Higgsfield MCP is connected on Bharath's account (image generation about 2.75 credits per high-quality 2K image; balance about 370 credits at the end of this session; video models cost more, so check with `get_cost: true` before generating). Generate a **character sheet** first so the characters stay consistent.
7. **Voiceover** (Telugu and English) → **animation and edit** → **captions burned in**.
8. **Final review checklist:**
   - facts match the source;
   - no Rule 36 phrases;
   - disclaimer on screen;
   - CTA is informational;
   - no real people, projects or logos;
   - the caption links the right page.
9. **Publish and schedule:**
   - The Metricool MCP is connected (social scheduling and analytics) and the Higgsfield MCP has TikTok publishing.
   - Canva needs authorising in claude.ai connector settings before use.
   - Suggested cadence: **3 shorts a week**, plus a longer YouTube cut per topic group once 4–5 shorts exist.
10. **Measure:** views, average watch %, saves, shares, and GA4 visits to the linked page (add `?utm_source=youtube&utm_medium=shorts&utm_campaign=<episode>` to caption links).

### 6.9 Sample script: A1 "Is this flat safe to buy? 4 documents to ask for" (English, about 55s)

| Time | Visual | Voiceover | On-screen text |
|---|---|---|---|
| 0–3s | Ravi's hand freezes over a booking cheque; the frame snaps to navy | "Before you pay for a flat in Tirupati, ask for these four documents." | **4 documents before you pay** |
| 3–10s | Ravi & Lakshmi at a site office; a glossy brochure sparkles, then fades to grey | "The brochure tells you about the balcony. It tells you nothing about whether the flat is legally safe." | Brochure ≠ title |
| 10–20s | A parchment card "1" slides in: sale deeds stacking back in time, then an EC sheet | "One: the title to the land the building stands on. The mother deed, the link documents, and the encumbrance certificate." | **1. Land title + EC** |
| 20–28s | Card "2": a RERA certificate with three highlighted lines | "Two: the project's RERA registration, and what it discloses about the promoter, the approvals and the timeline." | **2. RERA registration** |
| 28–36s | Card "3": a building plan unrolls with a gold "Sanctioned" stamp | "Three: the sanctioned building plan and permissions, so you are not buying an unauthorised or deviated construction." | **3. Building approvals** |
| 36–46s | Card "4": the agreement; three clauses glow red ("delay", "extra charges", "one-sided") | "Four: the builder agreement. Read it for one-sided clauses, hidden charges and unfair delivery terms before you sign." | **4. Builder agreement** |
| 46–53s | All four cards line up; gold ticks appear one by one | "Title. RERA. Approvals. Agreement. Check all four before the money leaves your hands." | Title · RERA · Approvals · Agreement |
| 53–60s | End card (navy, gold scales) | "The full checklist is on buklawpartners.com. Know the law before you sign." | buklawpartners.com · *General information, not legal advice. BUK Law Partners, Advocates, Tirupati.* |

Sources: `buying-a-flat-tirupati.html` ("What a Title Check on a Flat Covers"). Still to do: the Telugu version, and an independent check before production.

---

## 7. Tools, accounts and lessons from this session

- **Repo:** `bharathbudda/Atlas-Arise-bot` (**public**). Working branch `claude/busy-bohr-p4iavr`. When a PR from that branch has been merged, restart the branch from `origin/main` before new work.
- **Higgsfield (image generation):**
  - Model `gpt_image_2_5`, quality `high`, resolution `2k`.
  - **GIF references fail.** Convert GIFs to JPG first.
  - **Low-angle selfies distort AI portraits:** the head looks pasted on and too large. Use eye-level references, a reference for body build, and a separate reference for the setting, and say which reference is for what.
  - Describe the person's real build so the model doesn't slim or bulk them.
  - Images uploaded in chat are sometimes not saved as files, and mid-turn image messages may not be saved at all. Ask the user to upload through the Higgsfield upload widget, or check the session's images folder.
  - Uploading from the sandbox: `media_upload` → `curl -X PUT` with `Content-Type` **and** `If-None-Match: *` → `media_confirm`.
- **GitHub:** use the GitHub MCP tools (the `gh` CLI only for search). PRs need Bharath's explicit go-ahead; he approved and merged PR #1.
- **Verification habit that worked:**
  - after every change, load all pages in Playwright and check console errors and 404s;
  - check the pop-up and mobile overflow;
  - after a deploy, `curl` the live site for a marker string.
- **Background-process trap:** `pkill -f "<pattern>"` inside a Bash command that contains the same pattern kills that command. Stop servers by PID instead.

---

## 8. Open questions for Bharath (ask at the start of the next session)

1. **Video language:** Telugu-first with English subtitles plus an English version (recommended), or English only?
2. **Series name and characters:** approve "Know Before You Sign" and Ravi & Lakshmi / Ammamma / the scales mascot, or suggest others.
3. **Reference style:** which "What A Fact?" episodes does he like, and what about them?
4. **Voice:** AI narrator or a recorded human voice? Male or female? One voice for both languages?
5. **Channels:** which BUK social accounts exist (YouTube, Instagram, Facebook)? Handles? Who posts?
6. **Cadence:** 3 a week, or another number?
7. **District wording** on the website ("Tirupati and Chittoor districts"?).
8. **Housekeeping:** has he sent a test enquiry, turned on Netlify form emails, and submitted the sitemap to Search Console?
9. **Photos** of T. Kiran Kumar and K. Pramod Kumar Reddy.
10. **Repo visibility:** this repo is public. Should it be made private, or should the website and content work move to a dedicated private repo?
