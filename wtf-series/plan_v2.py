"""Season 1 v2 ('The Second Look'): scripts, beats, image prompts, budget.
Builds scripts_v2.html (the page for approval) and REVIEW_v2.md (compact copy for the independent check)."""
import html, pathlib
ROOT = pathlib.Path(__file__).parent
S = ROOT / "scripts_v2"
e = html.escape

STYLE = ("Bold flat 2D editorial cartoon illustration: thick confident dark navy (#13213C) ink outlines of even weight "
 "(white outlines where shapes sit on a dark navy sky), flat saturated fills with no gradients, limited palette of warm orange "
 "(#FF8C1A), dark navy, slate blue (#6F84A8), sky blue (#9CC3E6), sand (#F2D7A6) and white, one flat cel-shadow tone, subtle "
 "paper grain. Simple readable shapes, clear silhouette, expressive but not childish. Vertical 9:16 composition, main subject "
 "centred, top 12% and bottom 25% kept simple. No text, letters, numbers, logos or watermark; no photorealism; no 3D render.")
MARK = ("The same original mascot as the reference sheet: his head is the thick curved hook of a question mark in warm orange "
 "(#FF8C1A) with two navy dot eyes and eyebrows, floating above a small round dark navy body that forms the question mark's dot; "
 "short navy stick arms with white cartoon gloves, short legs with white sneakers. Bold flat 2D cartoon, thick even navy "
 "outlines, flat fills. Full body, single character, transparent background, no text, no shadow on the ground.")
MOTION = ("Animate this exact illustration. Keep the art style, line work, colours and composition identical: flat 2D cartoon, "
 "thick navy outlines. Smooth, gentle motion only; static camera, no camera shake, no new objects, no text.")

MARK_POSES = ["standing neutral, facing the viewer", "pointing to his left with one gloved finger", "shocked double-take: the curved hook snapped straight up into a vertical bar so his whole silhouette reads as an exclamation mark, hands on cheeks, small burst lines",
 "holding a large magnifying glass with a thick orange rim up to one eye", "shrugging with both palms up", "thumbs up, confident",
 "thinking, one hand on his chin, eyes looking up", "facepalm, one glove over his eyes", "jumping in celebration, both arms up",
 "peeking in from the side, only half his body visible, curious eyes", "holding a giant pencil like a lance", "holding up a large blank white index card with both hands"]

# Each beat: (VO line or cue, visual, source). Source codes: Ix = AI image (new), I1* = reused look-test image,
# Cx = AI clip from image, L = local (diagram, card, counter, lens), M = Mark pose overlay.
EPS = [
 dict(n="01", slug="gps", cat="TECH", hook="Claim: the clocks are set wrong on purpose", anchor="Satellite-clock counter card (µs per day)",
  lens="Over the '38 µs' index card; inside the lens the same card reads '≈ 11 km of ranging error'",
  imgs=[("I1*","Reused look-test satellite over Earth (job 22bd2d07); start frame for C1."),
        ("I2","A hand holding a smartphone showing a simple abstract map made of shapes only (no labels), one glowing slate-blue location dot."),
        ("I3","Four satellites spaced around a stylised Earth, dashed lines converging on one point on the surface."),
        ("I4","A round clock with no numerals floating above Earth; beneath Earth a curved spacetime grid dips like a stretched sheet."),
        ("I5","A GPS satellite streaking past with speed lines behind it, a small clock with no numerals mounted on its body."),
        ("I6","A thin bright beam of light racing from a satellite down to Earth, with motion streaks."),
        ("I7","An engineer's gloved hand turning a tiny dial on a satellite's clock module in a clean room, a rocket silhouette behind. Clock face has no numerals."),
        ("I8","A person walking down a city street at dusk looking at a phone, a glowing slate-blue dot trail behind them.")],
  clip=("C1 from I1*","the satellite glides along its dashed orbit; signal rings pulse toward the pin"),
  beats=[("The clocks on GPS satellites are set wrong. On purpose.","C1 hook clip, push-in; Mark peeks in on 'On purpose'","C1, M"),
         ("GPS is a timing machine…","I2 phone, then I3 satellites converge (local animated signal lines)","I2, I3, L"),
         ("…clocks tick faster in weaker gravity. About forty-five microseconds a day faster.","I4 spacetime grid; counter card ticks to +45","I4, L"),
         ("…moving clocks tick slower. About seven microseconds.","I5 speed-line satellite; counter ticks down to +38","I5, L"),
         ("Net result: thirty-eight microseconds fast, every day. Sounds tiny.","Notebook: bar diagram +45 / −7 / +38; Mark shrugs","L, M"),
         ("Wait.","Freeze and grey; lens slides over the '38 µs' card and reveals '≈ 11 km'; Mark '?'→'!'","L, M"),
         ("…worth more than ten kilometres of error. Per day.","I6 light beam; ranging-error bar grows past 10 km (no map drift)","I6, L"),
         ("…engineers tune each clock to tick slightly slow…","I7 engineer's hand on the dial","I7"),
         ("So the next time that blue dot finds you, remember…","I8 street at dusk, then hard loop cut to the hook","I8")]),
 dict(n="02", slug="whale", cat="EVOLUTION", hook="Claim, then an immediate 'Wait.'", anchor="Family-tree card that grows through the episode",
  lens="Over the hippo's reflection; inside the lens it is clearly a whale (the test clip, already built)",
  imgs=[("I1*","Reused hippo with whale reflection (job 621193dd) and its clip C1 (already made)."),
        ("I2","A shark and a seal side by side, looking puzzled."),
        ("I3","A DNA double helix with small orange segments hovering beside it, as if about to slot in."),
        ("I4","Two darts stuck in exactly the same tiny spot on a plain dartboard with no numbers on the rim."),
        ("I5","Fossil skeleton of a small, wolf-sized, four-legged early whale embedded in layered rock."),
        ("I6","A small hoofed mammal standing at a riverbank at dawn, the shared ancestor, its outline slightly faded."),
        ("I7","Split scene: on the left a hippo wallowing in a muddy river, on the right a whale gliding through the open ocean, a single wavy line dividing them.")],
  clip=("C1 from I1* (done)","the hippo blinks and the whale reflection ripples"),
  beats=[("A whale's closest living relative is a hippo.","C1 hook clip with push-in","C1"),
         ("Wait.","Freeze and grey; lens reveals the whale reflection; Mark '?'→'!'","L, M"),
         ("Family trees aren't built on looks. They're built on ancestry.","Notebook family-tree card draws on; shared-ancestor circle; Mark points","L, M"),
         ("The clincher came from DNA… jumping genes…","I3 helix (push-in), then local DNA strips: insert in whale + hippo, missing in cow/deer","I3, L"),
         ("The same random spot, twice?","I4 darts; Mark thinking","I4, M"),
         ("Then the fossils agreed… double-pulley ankle bone…","I5 fossil, then local ankle-bone diagram with the two grooves highlighted","I5, L"),
         ("So no, whales didn't evolve from hippos. They're cousins…","I6 ancestor at the riverbank; tree card updates with '50+ million years'","I6, L"),
         ("One family ended up wallowing in rivers. The other went all in on the ocean.","I7 split scene","I7"),
         ("So next time someone asks you what a whale's closest living relative is…","Back on I2 for a beat, then hard loop cut to the hook","I2")]),
 dict(n="03", slug="notes", cat="MUSIC", hook="Question", anchor="A 12-key strip at the top of the frame that lights up step by step",
  lens="Over the top of the spiral staircase; inside the lens the small overshoot gap is visible",
  imgs=[("I1","A piano keyboard seen from above showing exactly one octave: 7 white keys and 5 black keys in groups of 2 and 3, glowing orange edges."),
        ("I2","A cartoon ear and a pocket calculator (blank display, unlabelled buttons) standing side by side, almost touching."),
        ("I3","A single string stretched on a long wooden board (a monochord), a finger plucking it, faint vibration curves."),
        ("I4","A spiral staircase of twelve steps winding upward through seven floors; a small orange ball lands on the top step, just past the edge of the top floor, leaving a tiny gap."),
        ("I5","A piano tuner with a tuning lever leaning into an open upright piano, nineteenth-century clothes."),
        ("I6","A sitar and a tanpura resting on a patterned rug."),
        ("I7","A row of bronze gamelan metallophones with mallets."),
        ("I8","A cartoon ear and a piano keyboard shaking hands.")],
  clip=("C1 from I1","the keys press down one after another in a wave, soft light pulsing"),
  beats=[("Every piano repeats itself after twelve keys. Why twelve?","C1 hook clip; 12-key strip appears; Mark thinking","C1, L, M"),
         ("Because twelve is where maths and your ears almost agree.","I2 ear and calculator","I2"),
         ("Notes sound good together when their frequencies form simple ratios…","I3 monochord, then local waveforms 2:1 and 3:2 with real tones","I3, L"),
         ("Now stack fifths… seven octaves up.","I4 staircase with push-in; the key strip lights step by step","I4, L"),
         ("Wait. Almost?","Freeze and grey; lens over the top step shows the gap; Mark '?'→'!'","L, M"),
         ("Twelve fifths multiply the frequency by 129.7. Seven octaves give exactly 128…","Notebook: 129.7 vs 128 bars, 'Pythagorean comma ≈ 23.5 cents' card","L"),
         ("Over centuries, musicians settled on a compromise…","I5 piano tuner, then a local circle of 12 equal slices closing","I5, L"),
         ("It's not universal. Indian music theory… gamelan…","I6 sitar and tanpura, then I7 gamelan","I6, I7"),
         ("Twelve isn't magic. It's the best deal our ears would accept. That's why…","I8 handshake, then hard loop cut to the hook","I8")]),
 dict(n="04", slug="bacteria", cat="BIOLOGY", hook="Myth to bust, in the second person", anchor="Scoreboard card: 'BACTERIA vs YOU'",
  lens="Over the hook silhouette; inside the lens the body is packed with red blood cells (truth image I5)",
  imgs=[("I1","A human silhouette outline filled with hundreds of tiny orange rod- and dot-shaped bacteria."),
        ("I2","A 1970s desk with a typewriter, a coffee mug, and a blank sheet covered in wavy pencil lines."),
        ("I3","A scientist at a desk with stacks of blank papers and a calculator (blank display, unlabelled buttons)."),
        ("I4","A stylised winding intestine tube, friendly and non-gory, filled with tiny orange bacteria."),
        ("I5","Dozens of red blood cells (red-orange biconcave discs) flowing through a vessel, filling the frame."),
        ("I6","An old balance scale with a single mango on one pan and a small heap of tiny orange bacteria on the other, level."),
        ("I7","A seesaw with a cartoon human on one end and a cloud of bacteria on the other, perfectly level."),
        ("I7b","Edit of I7 using it as reference: the same seesaw now tipped so the human's end is down."),
        ("I8","The same human silhouette standing confidently, glowing softly, a few bacteria orbiting around it.")],
  clip=("C1 from I1","the bacteria swirl slowly inside the silhouette like a gentle current"),
  beats=[("You've been told you're more bacteria than human. Ten microbes for every one of your cells.","C1 hook clip; '10 : 1' stamp","C1, L"),
         ("That number came from a back-of-the-envelope estimate in 1972…","I2 desk; '10 : 1' struck through; Mark facepalm","I2, L, M"),
         ("In 2016, researchers… made a careful estimate…","I3 scientist, then I4 gut tube; scoreboard 38 T vs 30 T","I3, I4, L"),
         ("So not ten to one. Roughly one point three to one.","Scoreboard card 1.3 : 1","L"),
         ("Wait. It gets better.","Freeze I1 and grey; lens shows red blood cells (I5) inside the body; Mark '?'→'!'","L, I5, M"),
         ("Most of your own cells are red blood cells… Roughly one mango.","I5 full frame, donut chart 84%, then I6 scale","I5, L, I6"),
         ("The ratio isn't even fixed… toilet…","I7 seesaw level, then I7b tipped","I7, I7b"),
         ("By count, it's close to a tie. By weight, you're overwhelmingly you…","I8 silhouette; Mark thumbs up; hard loop cut to the hook","I8, M")]),
 dict(n="05", slug="ok", cat="LANGUAGE", hook="Claim with an aside", anchor="A year ticker (1838 → 1839 → 1840 → 1963)",
  lens="Over the blank newspaper column; inside the lens the tiny printed 'o.k.' appears (overlaid locally)",
  imgs=[("I1","A vintage hand-operated printing press with a sheet of paper; solid blank areas, no print."),
        ("I2","An 1830s Boston street, a newsboy in a cap holding up newspapers with solid blank pages and no print."),
        ("I3","Close-up of an old newspaper page made of solid blank column blocks, no print."),
        ("I4","A wastebasket full of crumpled paper with one sheet floating up out of it."),
        ("I5","An 1840 election rally: top hats, a crowd, banners made of solid blank cloth with no print."),
        ("I6","A generic nineteenth-century American statesman with large sideburns in a dark coat; not a portrait likeness."),
        ("I7","A 1960s linguist in a library among stacks of old newspapers with solid blank pages and no print, holding a magnifying glass."),
        ("I8","A modern hand typing on a smartphone with a blank screen.")],
  clip=("C1 from I1","the press lever pulls down and stamps the sheet; a puff of ink dust"),
  beats=[("\"OK\" might be the most successful joke ever told.","C1 hook clip; Mark grins in with a thumbs up","C1, M"),
         ("In the late 1830s, Boston newspapers had a craze… O.W.… K.G.…","I2 street; local index cards flip O.W. / K.G.; year ticker 1838","I2, L"),
         ("On the twenty-third of March, 1839… 'oll korrect'.","I3 page with local overlay 'o.k. — all correct'; ticker 1839","I3, L"),
         ("Most of these jokes died. OK got lucky.","I4 wastebasket","I4"),
         ("In 1840, President Martin Van Buren… O.K. Clubs…","I5 rally (push-in), I6 statesman; local 'O.K.' on a banner; ticker 1840","I5, I6, L"),
         ("Van Buren lost. The word won.","Local scoreboard card; Mark shrugs","L, M"),
         ("Wait. Nobody pieced this together until the 1960s…","Freeze I3 and grey; lens finds the tiny 'o.k.'; then I7 linguist; ticker 1963","L, I7, M"),
         ("So every time you text \"OK\", you're finishing a joke from 1839. Which is why…","I8 phone with local 'ok' bubble; hard loop cut to the hook","I8, L")]),
 dict(n="06", slug="windows", cat="ENGINEERING", hook="Myth, half right", anchor="A flight-cycle counter (0 → about 1,000)",
  lens="Over the Comet's passenger windows in I2; inside the lens the corners are clearly rounded",
  imgs=[("I1","Close-up of a modern airliner cabin window with rounded corners, clouds outside."),
        ("I2","A 1950s jet airliner in flight: sleek unpainted silver body, unmarked with no airline livery, four engines buried in the wing roots, small rounded-rectangle cabin windows."),
        ("I3","A salvage ship with a crane on a calm sea at dusk."),
        ("I4","An airliner fuselage submerged in a huge indoor water tank, engineers on a gantry above."),
        ("I5","Edit of I4 using it as reference: the same tank scene with the fuselage split open along a jagged crack."),
        ("I6","Top of an aircraft fuselage with two small rectangular antenna cut-outs in the roof, an orange crack spreading from one corner."),
        ("I7","A fuselage section gently swelling and relaxing like a breathing balloon, with curved arrows."),
        ("I8","Macro close-up of a hairline crack growing from the corner of a hole in an aluminium sheet."),
        ("I9","Engineers with a flashlight inspecting the rounded window frames of a modern airliner.")],
  clip=("C1 from I1","clouds drift past outside the window; light shifts gently"),
  beats=[("You've probably heard plane windows are round because square ones made jets crash. That's only half right.","C1 hook clip; local square-window icon struck through","C1, L"),
         ("In 1954, two de Havilland Comets… broke apart in mid-air…","I2 Comet, then I3 salvage ship","I2, I3"),
         ("Investigators sank an entire Comet fuselage in a giant water tank…","I4 tank; flight-cycle counter ticks up; I5 split","I4, I5, L"),
         ("Wait.","Freeze I2 and grey; lens shows the rounded passenger windows; Mark '?'→'!'","L, M"),
         ("…just tightly rounded… began at the corner of a small antenna window in the roof.","Local window-shape comparison card, then I6 roof cut-outs with a highlight ring","L, I6"),
         ("Every flight, the cabin swells slightly, then relaxes…","I7 breathing fuselage, then local stress-line diagram (sharp vs rounded)","I7, L"),
         ("After about a thousand flights, the metal cracked.","I8 crack macro; counter stops at about 1,000","I8, L"),
         ("So the real lesson… design every opening for fatigue. So next time someone tells you…","I9 inspection; Mark points; hard loop cut to the hook","I9, M")]),
]

# ---- budget (live quotes, 4 Nov 2026)
new_imgs = sum(1 for ep in EPS for code, _ in ep["imgs"] if not code.endswith("*"))
BUDGET = [
 ("Done", "Look test (6 images)", 10.5),
 ("Done", "EP02 test: hook clip + 3 VO lines", 5.92),
 ("P1", "Mark pose pack: 12 poses, GPT Image 2.5 high 1K, transparent @1.5", 18.0),
 ("P1", "Brand music bed: ElevenLabs Music v2.5, 60 s, 2 takes @8.72", 17.44),
 ("P2", f"Scene images: {new_imgs} new, GPT Image 2.5 high 2K @2.75 (2 reused from the look test)", round(new_imgs * 2.75, 2)),
 ("P3", "Hook clips: 5 new (EP02 done), Seedance 2.0 Mini 720p 5 s @5.0", 25.0),
 ("P4", "Voiceover: Ainsley, ElevenLabs v4, by line, ≈5 per episode (EP02 partly done)", 28.0),
]
CAP = 297.0
total = round(sum(b[2] for b in BUDGET), 2)
reserve = round(CAP - total, 2)

def words(t): return len(t.split())

md = [f"# WTF Season 1 v2 review copy\nCap {CAP}. Planned total incl. spent {total}. Headroom {reserve}.\n",
      f"Image style block:\n> {STYLE}\n", f"Mark block:\n> {MARK}\n", f"Clip motion block:\n> {MOTION}\n", "## Budget"] + \
     [f"- {a} | {b} | {c}" for a, b, c in BUDGET]
for ep in EPS:
    sc = (S / f"ep{ep['n']}_{ep['slug']}_v2.txt").read_text().strip()
    md += [f"\n## EP{ep['n']} {ep['cat']} — {words(sc)} words (Ainsley ≈150 wpm → ≈{words(sc)/150*60:.0f}s)",
           f"Hook type: {ep['hook']}. Anchor: {ep['anchor']}. Lens: {ep['lens']}.", "### Script", sc, "### Images"] + \
          [f"- {c}: {p}" for c, p in ep["imgs"]] + [f"- Clip {ep['clip'][0]}: {ep['clip'][1]}", "### Beats"] + \
          [f"- {v} → {vis} [{src}]" for v, vis, src in ep["beats"]]
(ROOT / "REVIEW_v2.md").write_text("\n".join(md))

# ---- page
def ep_html(ep):
    sc = (S / f"ep{ep['n']}_{ep['slug']}_v2.txt").read_text().strip()
    paras = "".join(f"<p{' class=wait' if p.strip().startswith('Wait') else ''}>{e(p)}</p>" for p in sc.split("\n"))
    beats = "".join(f"<tr><td>{e(v)}</td><td>{e(vis)}</td><td class=src>{e(s)}</td></tr>" for v, vis, s in ep["beats"])
    imgs = "".join(f"<li><b>{e(c)}</b> {e(p)}</li>" for c, p in ep["imgs"])
    w = words(sc)
    return f"""<section class=ep id=ep{ep['n']}><header><span class=pill>FACT {ep['n']}</span><span class=cat>{ep['cat']}</span>
<p class=meta>{w} words · about {w/150*60:.0f} s at Ainsley's pace · hook: {e(ep['hook'])}</p></header>
<div class=two><div class=script><h4>Script</h4>{paras}<p class=loop>↺ loops straight back into the first line</p></div>
<div><h4>Signature moments</h4><ul class=sig><li><b>Lens:</b> {e(ep['lens'])}</li><li><b>Anchor:</b> {e(ep['anchor'])}</li><li><b>Hook clip:</b> {e(ep['clip'][0])}: {e(ep['clip'][1])}</li></ul>
<h4>Images to generate</h4><ul class=imgs>{imgs}</ul></div></div>
<h4>Beats (timed to the recorded voice in the edit)</h4><div class=tw><table><thead><tr><th>Voice</th><th>Picture</th><th>Source</th></tr></thead><tbody>{beats}</tbody></table></div></section>"""

brows = "".join(f"<tr><td>{a}</td><td>{e(b)}</td><td class=num>{c:.2f}</td></tr>" for a, b, c in BUDGET)
page = f"""<title>WTF Season 1 Scripts</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Caveat:wght@700&family=JetBrains+Mono:wght@500;700&display=swap">
<style>
/* Layout: approval box, budget, then six episode chapters with script beside its signature moments. */
:root{{--bg:#F4F6FA;--paper:#FFFFFF;--ink:#13213C;--muted:#55627A;--line:#D9DFEA;--accent:#E0700A;--chip:#FFE6CC;
 --display:'Bricolage Grotesque',system-ui,sans-serif;--hand:'Caveat',cursive;--mono:'JetBrains Mono',ui-monospace,monospace}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#0E1830;--paper:#13213C;--ink:#EEF2F8;--muted:#9AA9C4;--line:#24365E;--accent:#FF8C1A;--chip:#3A2A17;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0E1830;--paper:#13213C;--ink:#EEF2F8;--muted:#9AA9C4;--line:#24365E;--accent:#FF8C1A;--chip:#3A2A17;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font:500 16px/1.55 var(--display);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.wrap{{max-width:1080px;margin:0 auto;padding-block:32px 80px;display:grid;gap:32px}}
h1,h2{{font-weight:800;line-height:1.08;text-wrap:balance;margin:0}} h1{{font-size:clamp(30px,5vw,48px);letter-spacing:-.02em}} h2{{font-size:26px}}
h4{{font:700 12px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:14px 0 8px}}
p{{margin:0 0 8px;max-width:66ch}} .eyebrow{{font:700 13px var(--mono);letter-spacing:.14em;color:var(--accent);text-transform:uppercase}}
.box{{background:var(--paper);border:2px solid var(--accent);border-radius:14px;padding:18px 20px;display:grid;gap:8px}}
.box ol{{margin:0;padding-left:20px;display:grid;gap:6px}}
.tw{{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--paper)}}
table{{border-collapse:collapse;width:100%;font-size:14px;min-width:620px}} th,td{{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line)}}
th{{font:700 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}}
td.num{{text-align:right;font:700 14px var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}} td.src{{font:700 12px var(--mono);white-space:nowrap;color:var(--muted)}}
tfoot td{{font-weight:800}}
.ep{{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:20px 22px;display:grid;gap:4px;scroll-margin-top:16px}}
.ep header{{display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
.pill{{background:var(--accent);color:#13213C;font:700 12px var(--mono);letter-spacing:.1em;padding:3px 10px;border-radius:7px}}
.cat{{font:700 12px var(--mono);letter-spacing:.14em;color:var(--muted)}} .meta{{margin:0;color:var(--muted);font-size:14px;flex-basis:100%}}
.two{{display:grid;grid-template-columns:1.05fr 1fr;gap:24px}} .two>div{{min-width:0}}
.script p.wait{{font:800 22px var(--display);color:var(--accent)}} .loop{{font:700 22px var(--hand);color:var(--accent)}}
.sig,.imgs{{margin:0;padding-left:18px;display:grid;gap:5px;font-size:14.5px}}
nav{{display:flex;gap:8px;flex-wrap:wrap}} nav a{{font:700 13px var(--mono);text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:4px 10px;background:var(--paper);color:var(--accent)}}
.block{{background:var(--paper);border:1px dashed var(--line);border-radius:10px;padding:12px 14px;font:500 13px/1.5 var(--mono);overflow-wrap:anywhere}}
@media (max-width:760px){{.two{{grid-template-columns:1fr}}}}
</style>
<div class=wrap>
<header style="display:grid;gap:12px"><span class=eyebrow>Wait, That's a Fact? · Season 1 · scripts v2, "The Second Look"</span>
<h1>Six scripts, ready for your sign-off</h1>
<p style="color:var(--muted);font-size:17px">Rewritten to the audit's rules: a hook in the first second, a different hook shape in each episode, a "Wait." twist with the lens and Mark, one anchor graphic per episode, and endings that loop back into the hook. All facts are from the verified list, and an independent agent checked this version before it reached you.</p>
<nav>{''.join(f"<a href='#ep{x['n']}'>EP{x['n']}</a>" for x in EPS)}</nav></header>
<section class=box><h2>When you approve, the credit-spending steps run today</h2><ol>
<li>Mark's pose pack and the music bed (≈35 cr)</li><li>{new_imgs} scene images in batches, each checked before the next batch (≈{new_imgs*2.75:.0f} cr)</li>
<li>5 hook clips (25 cr)</li><li>All voiceover by line (≈28 cr)</li><li>Then the edit, which costs nothing and can continue after the credits expire</li></ol>
<p style="margin:0"><b>Total including what's already spent: {total:.1f} of {CAP:.0f}</b>, leaving {reserve:.1f} for retakes.</p></section>
<section style="display:grid;gap:10px"><h2>Budget</h2><div class=tw><table><thead><tr><th>Phase</th><th>Item</th><th>Credits</th></tr></thead><tbody>{brows}</tbody>
<tfoot><tr><td></td><td>Total incl. spent</td><td class=num>{total:.2f}</td></tr></tfoot></table></div></section>
{''.join(ep_html(x) for x in EPS)}
<section style="display:grid;gap:8px"><h2>Prompt blocks</h2><h4>Appended to every scene prompt</h4><div class=block>{e(STYLE)}</div>
<h4>Every Mark pose (with the approved sheet as reference)</h4><div class=block>{e(MARK)}</div><h4>Every clip</h4><div class=block>{e(MOTION)}</div></section>
</div>"""
(ROOT / "scripts_v2.html").write_text(page)
print("new images", new_imgs, "total", total, "reserve", reserve)
