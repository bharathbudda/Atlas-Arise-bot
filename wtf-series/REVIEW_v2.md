# WTF Season 1 v2 review copy
Cap 297.0. Planned total incl. spent 234.11. Headroom 62.89.

Image style block:
> Bold flat 2D editorial cartoon illustration: thick confident dark navy (#13213C) ink outlines of even weight (white outlines where shapes sit on a dark navy sky), flat saturated fills with no gradients, limited palette of warm orange (#FF8C1A), dark navy, slate blue (#6F84A8), sky blue (#9CC3E6), sand (#F2D7A6) and white, one flat cel-shadow tone, subtle paper grain. Simple readable shapes, clear silhouette, expressive but not childish. Vertical 9:16 composition, main subject centred, top 12% and bottom 25% kept simple. No text, letters, numbers, logos or watermark; no photorealism; no 3D render.

Mark block:
> The same original mascot as the reference sheet: his head is the thick curved hook of a question mark in warm orange (#FF8C1A) with two navy dot eyes and eyebrows, floating above a small round dark navy body that forms the question mark's dot; short navy stick arms with white cartoon gloves, short legs with white sneakers. Bold flat 2D cartoon, thick even navy outlines, flat fills. Full body, single character, transparent background, no text, no shadow on the ground.

Clip motion block:
> Animate this exact illustration. Keep the art style, line work, colours and composition identical: flat 2D cartoon, thick navy outlines. Smooth, gentle motion only; static camera, no camera shake, no new objects, no text.

## Budget
- Done | Look test (6 images) | 10.5
- Done | EP02 test: hook clip + 3 VO lines | 5.92
- P1 | Mark pose pack: 12 poses, GPT Image 2.5 high 1K, transparent @1.5 | 18.0
- P1 | Brand music bed: ElevenLabs Music v2.5, 60 s, 2 takes @8.72 | 17.44
- P2 | Scene images: 47 new, GPT Image 2.5 high 2K @2.75 (2 reused from the look test) | 129.25
- P3 | Hook clips: 5 new (EP02 done), Seedance 2.0 Mini 720p 5 s @5.0 | 25.0
- P4 | Voiceover: Ainsley, ElevenLabs v4, by line, ≈5 per episode (EP02 partly done) | 28.0

## EP01 TECH — 139 words (Ainsley ≈150 wpm → ≈56s)
Hook type: Claim: the clocks are set wrong on purpose. Anchor: Satellite-clock counter card (µs per day). Lens: Over the '38 µs' index card; inside the lens the same card reads '≈ 11 km of ranging error'.
### Script
The clocks on GPS satellites are set wrong. On purpose.
GPS is a timing machine. Satellites twenty thousand kilometres up broadcast the exact time, and your phone works out where you are from how long each signal took to arrive.
Up there, gravity is weaker, and Einstein's relativity says clocks tick faster in weaker gravity. About forty-five microseconds a day faster.
But the satellites also fly at nearly four kilometres a second, and moving clocks tick slower. About seven microseconds.
Net result: thirty-eight microseconds fast, every day. Sounds tiny.
Wait.
The signals travel at the speed of light, so that drift is worth more than ten kilometres of error. Per day.
So before launch, engineers tune each clock to tick slightly slow, and in orbit it keeps near-perfect time.
So the next time that blue dot finds you, remember...
### Images
- I1*: Reused look-test satellite over Earth (job 22bd2d07); start frame for C1.
- I2: A hand holding a smartphone showing a simple abstract map made of shapes only (no labels), one glowing slate-blue location dot.
- I3: Four satellites spaced around a stylised Earth, dashed lines converging on one point on the surface.
- I4: A round clock with no numerals floating above Earth; beneath Earth a curved spacetime grid dips like a stretched sheet.
- I5: A GPS satellite streaking past with speed lines behind it, a small clock with no numerals mounted on its body.
- I6: A thin bright beam of light racing from a satellite down to Earth, with motion streaks.
- I7: An engineer's gloved hand turning a tiny dial on a satellite's clock module in a clean room, a rocket silhouette behind. Clock face has no numerals.
- I8: A person walking down a city street at dusk looking at a phone, a glowing slate-blue dot trail behind them.
- Clip C1 from I1*: the satellite glides along its dashed orbit; signal rings pulse toward the pin
### Beats
- The clocks on GPS satellites are set wrong. On purpose. → C1 hook clip, push-in; Mark peeks in on 'On purpose' [C1, M]
- GPS is a timing machine… → I2 phone, then I3 satellites converge (local animated signal lines) [I2, I3, L]
- …clocks tick faster in weaker gravity. About forty-five microseconds a day faster. → I4 spacetime grid; counter card ticks to +45 [I4, L]
- …moving clocks tick slower. About seven microseconds. → I5 speed-line satellite; counter ticks down to +38 [I5, L]
- Net result: thirty-eight microseconds fast, every day. Sounds tiny. → Notebook: bar diagram +45 / −7 / +38; Mark shrugs [L, M]
- Wait. → Freeze and grey; lens slides over the '38 µs' card and reveals '≈ 11 km'; Mark '?'→'!' [L, M]
- …worth more than ten kilometres of error. Per day. → I6 light beam; ranging-error bar grows past 10 km (no map drift) [I6, L]
- …engineers tune each clock to tick slightly slow… → I7 engineer's hand on the dial [I7]
- So the next time that blue dot finds you, remember… → I8 street at dusk, then hard loop cut to the hook [I8]

## EP02 EVOLUTION — 143 words (Ainsley ≈150 wpm → ≈57s)
Hook type: Claim, then an immediate 'Wait.'. Anchor: Family-tree card that grows through the episode. Lens: Over the hippo's reflection; inside the lens it is clearly a whale (the test clip, already built).
### Script
A whale's closest living relative is a hippo.
Wait.
Family trees aren't built on looks. They're built on ancestry.
The clincher came from DNA. In 1999, a team in Japan found "jumping genes", stretches of DNA that paste copies of themselves into the genome, sitting in the exact same spots in whales and hippos, and missing in cows and deer.
The same random spot, twice? That basically never happens by chance.
Then the fossils agreed. Ancient whales that still had legs turned up with a double-pulley ankle bone, the signature of even-toed hoofed mammals.
So no, whales didn't evolve from hippos. They're cousins, with a shared ancestor that lived more than fifty million years ago. One family ended up wallowing in rivers. The other went all in on the ocean.
So next time someone asks you what a whale's closest living relative is...
### Images
- I1*: Reused hippo with whale reflection (job 621193dd) and its clip C1 (already made).
- I2: A shark and a seal side by side, looking puzzled.
- I3: A DNA double helix with small orange segments hovering beside it, as if about to slot in.
- I4: Two darts stuck in exactly the same tiny spot on a plain dartboard with no numbers on the rim.
- I5: Fossil skeleton of a small, wolf-sized, four-legged early whale embedded in layered rock.
- I6: A small hoofed mammal standing at a riverbank at dawn, the shared ancestor, its outline slightly faded.
- I7: Split scene: on the left a hippo wallowing in a muddy river, on the right a whale gliding through the open ocean, a single wavy line dividing them.
- Clip C1 from I1* (done): the hippo blinks and the whale reflection ripples
### Beats
- A whale's closest living relative is a hippo. → C1 hook clip with push-in [C1]
- Wait. → Freeze and grey; lens reveals the whale reflection; Mark '?'→'!' [L, M]
- Family trees aren't built on looks. They're built on ancestry. → Notebook family-tree card draws on; shared-ancestor circle; Mark points [L, M]
- The clincher came from DNA… jumping genes… → I3 helix (push-in), then local DNA strips: insert in whale + hippo, missing in cow/deer [I3, L]
- The same random spot, twice? → I4 darts; Mark thinking [I4, M]
- Then the fossils agreed… double-pulley ankle bone… → I5 fossil, then local ankle-bone diagram with the two grooves highlighted [I5, L]
- So no, whales didn't evolve from hippos. They're cousins… → I6 ancestor at the riverbank; tree card updates with '50+ million years' [I6, L]
- One family ended up wallowing in rivers. The other went all in on the ocean. → I7 split scene [I7]
- So next time someone asks you what a whale's closest living relative is… → Back on I2 for a beat, then hard loop cut to the hook [I2]

## EP03 MUSIC — 144 words (Ainsley ≈150 wpm → ≈58s)
Hook type: Question. Anchor: A 12-key strip at the top of the frame that lights up step by step. Lens: Over the top of the spiral staircase; inside the lens the small overshoot gap is visible.
### Script
Every piano repeats itself after twelve keys. Why twelve?
Because twelve is where maths and your ears almost agree.
Notes sound good together when their frequencies form simple ratios. Double the frequency and you get the same note, an octave higher. Multiply by three over two and you get a fifth, the smoothest-sounding interval after the octave.
Now stack fifths. After twelve of them, you land almost exactly seven octaves up.
Wait. Almost?
Twelve fifths multiply the frequency by 129.7. Seven octaves give exactly 128. That gap is the Pythagorean comma.
Over centuries, musicians settled on a compromise. Shrink every fifth by a hair, and twelve equal steps fit the octave perfectly.
It's not universal. Indian music theory describes twenty-two shrutis, and Javanese gamelan uses scales of five or seven tones.
Twelve isn't magic. It's the best deal our ears would accept. That's why...
### Images
- I1: A piano keyboard seen from above showing exactly one octave: 7 white keys and 5 black keys in groups of 2 and 3, glowing orange edges.
- I2: A cartoon ear and a pocket calculator (blank display, unlabelled buttons) standing side by side, almost touching.
- I3: A single string stretched on a long wooden board (a monochord), a finger plucking it, faint vibration curves.
- I4: A spiral staircase of twelve steps winding upward through seven floors; a small orange ball lands on the top step, just past the edge of the top floor, leaving a tiny gap.
- I5: A piano tuner with a tuning lever leaning into an open upright piano, nineteenth-century clothes.
- I6: A sitar and a tanpura resting on a patterned rug.
- I7: A row of bronze gamelan metallophones with mallets.
- I8: A cartoon ear and a piano keyboard shaking hands.
- Clip C1 from I1: the keys press down one after another in a wave, soft light pulsing
### Beats
- Every piano repeats itself after twelve keys. Why twelve? → C1 hook clip; 12-key strip appears; Mark thinking [C1, L, M]
- Because twelve is where maths and your ears almost agree. → I2 ear and calculator [I2]
- Notes sound good together when their frequencies form simple ratios… → I3 monochord, then local waveforms 2:1 and 3:2 with real tones [I3, L]
- Now stack fifths… seven octaves up. → I4 staircase with push-in; the key strip lights step by step [I4, L]
- Wait. Almost? → Freeze and grey; lens over the top step shows the gap; Mark '?'→'!' [L, M]
- Twelve fifths multiply the frequency by 129.7. Seven octaves give exactly 128… → Notebook: 129.7 vs 128 bars, 'Pythagorean comma ≈ 23.5 cents' card [L]
- Over centuries, musicians settled on a compromise… → I5 piano tuner, then a local circle of 12 equal slices closing [I5, L]
- It's not universal. Indian music theory… gamelan… → I6 sitar and tanpura, then I7 gamelan [I6, I7]
- Twelve isn't magic. It's the best deal our ears would accept. That's why… → I8 handshake, then hard loop cut to the hook [I8]

## EP04 BIOLOGY — 147 words (Ainsley ≈150 wpm → ≈59s)
Hook type: Myth to bust, in the second person. Anchor: Scoreboard card: 'BACTERIA vs YOU'. Lens: Over the hook silhouette; inside the lens the body is packed with red blood cells (truth image I5).
### Script
You've been told you're more bacteria than human. Ten microbes for every one of your cells.
That number came from a back-of-the-envelope estimate in 1972, and it got repeated for more than forty years.
In 2016, researchers in Israel and Canada finally made a careful estimate. About thirty-eight trillion bacteria, mostly in your colon. About thirty trillion human cells.
So not ten to one. Roughly one point three to one.
Wait. It gets better.
Most of your own cells are red blood cells, about eighty-four percent of them. And bacteria are tiny. All of yours together weigh about two hundred grams. Roughly one mango.
The ratio isn't even fixed. A single trip to the toilet can flush out enough gut bacteria to tip the balance back toward you.
By count, it's close to a tie. By weight, you're overwhelmingly you. So the next time someone tells you...
### Images
- I1: A human silhouette outline filled with hundreds of tiny orange rod- and dot-shaped bacteria.
- I2: A 1970s desk with a typewriter, a coffee mug, and a blank sheet covered in wavy pencil lines.
- I3: A scientist at a desk with stacks of blank papers and a calculator (blank display, unlabelled buttons).
- I4: A stylised winding intestine tube, friendly and non-gory, filled with tiny orange bacteria.
- I5: Dozens of red blood cells (red-orange biconcave discs) flowing through a vessel, filling the frame.
- I6: An old balance scale with a single mango on one pan and a small heap of tiny orange bacteria on the other, level.
- I7: A seesaw with a cartoon human on one end and a cloud of bacteria on the other, perfectly level.
- I7b: Edit of I7 using it as reference: the same seesaw now tipped so the human's end is down.
- I8: The same human silhouette standing confidently, glowing softly, a few bacteria orbiting around it.
- Clip C1 from I1: the bacteria swirl slowly inside the silhouette like a gentle current
### Beats
- You've been told you're more bacteria than human. Ten microbes for every one of your cells. → C1 hook clip; '10 : 1' stamp [C1, L]
- That number came from a back-of-the-envelope estimate in 1972… → I2 desk; '10 : 1' struck through; Mark facepalm [I2, L, M]
- In 2016, researchers… made a careful estimate… → I3 scientist, then I4 gut tube; scoreboard 38 T vs 30 T [I3, I4, L]
- So not ten to one. Roughly one point three to one. → Scoreboard card 1.3 : 1 [L]
- Wait. It gets better. → Freeze I1 and grey; lens shows red blood cells (I5) inside the body; Mark '?'→'!' [L, I5, M]
- Most of your own cells are red blood cells… Roughly one mango. → I5 full frame, donut chart 84%, then I6 scale [I5, L, I6]
- The ratio isn't even fixed… toilet… → I7 seesaw level, then I7b tipped [I7, I7b]
- By count, it's close to a tie. By weight, you're overwhelmingly you… → I8 silhouette; Mark thumbs up; hard loop cut to the hook [I8, M]

## EP05 LANGUAGE — 126 words (Ainsley ≈150 wpm → ≈50s)
Hook type: Claim with an aside. Anchor: A year ticker (1838 → 1839 → 1840 → 1963). Lens: Over the blank newspaper column; inside the lens the tiny printed 'o.k.' appears (overlaid locally).
### Script
"OK" might be the most successful joke ever told.
In the late 1830s, Boston newspapers had a craze for abbreviating deliberately misspelled phrases. O.W., "oll wright". K.G., "know go".
On the twenty-third of March, 1839, the Boston Morning Post printed "o.k.", short for "all correct", jokingly spelled "oll korrect".
Most of these jokes died. OK got lucky.
In 1840, President Martin Van Buren ran for re-election. His nickname was "Old Kinderhook", after his hometown. Supporters formed O.K. Clubs, and suddenly two letters were everywhere.
Van Buren lost. The word won.
Wait. Nobody pieced this together until the 1960s, when linguist Allen Walker Read dug through old newspapers and followed the trail.
So every time you text "OK", you're finishing a joke from 1839. Which is why...
### Images
- I1: A vintage hand-operated printing press with a sheet of paper; solid blank areas, no print.
- I2: An 1830s Boston street, a newsboy in a cap holding up newspapers with solid blank pages and no print.
- I3: Close-up of an old newspaper page made of solid blank column blocks, no print.
- I4: A wastebasket full of crumpled paper with one sheet floating up out of it.
- I5: An 1840 election rally: top hats, a crowd, banners made of solid blank cloth with no print.
- I6: A generic nineteenth-century American statesman with large sideburns in a dark coat; not a portrait likeness.
- I7: A 1960s linguist in a library among stacks of old newspapers with solid blank pages and no print, holding a magnifying glass.
- I8: A modern hand typing on a smartphone with a blank screen.
- Clip C1 from I1: the press lever pulls down and stamps the sheet; a puff of ink dust
### Beats
- "OK" might be the most successful joke ever told. → C1 hook clip; Mark grins in with a thumbs up [C1, M]
- In the late 1830s, Boston newspapers had a craze… O.W.… K.G.… → I2 street; local index cards flip O.W. / K.G.; year ticker 1838 [I2, L]
- On the twenty-third of March, 1839… 'oll korrect'. → I3 page with local overlay 'o.k. — all correct'; ticker 1839 [I3, L]
- Most of these jokes died. OK got lucky. → I4 wastebasket [I4]
- In 1840, President Martin Van Buren… O.K. Clubs… → I5 rally (push-in), I6 statesman; local 'O.K.' on a banner; ticker 1840 [I5, I6, L]
- Van Buren lost. The word won. → Local scoreboard card; Mark shrugs [L, M]
- Wait. Nobody pieced this together until the 1960s… → Freeze I3 and grey; lens finds the tiny 'o.k.'; then I7 linguist; ticker 1963 [L, I7, M]
- So every time you text "OK", you're finishing a joke from 1839. Which is why… → I8 phone with local 'ok' bubble; hard loop cut to the hook [I8, L]

## EP06 ENGINEERING — 146 words (Ainsley ≈150 wpm → ≈58s)
Hook type: Myth, half right. Anchor: A flight-cycle counter (0 → about 1,000). Lens: Over the Comet's passenger windows in I2; inside the lens the corners are clearly rounded.
### Script
You've probably heard plane windows are round because square ones made jets crash. That's only half right.
In 1954, two de Havilland Comets, the world's first jet airliners, broke apart in mid-air, less than three months apart.
Investigators sank an entire Comet fuselage in a giant water tank and pressurised it again and again, flight after simulated flight, until it split open.
Wait.
The Comet's passenger windows already had rounded corners, just tightly rounded. The inquiry found the first break-up most likely began at the corner of a small antenna window in the roof.
Every flight, the cabin swells slightly, then relaxes. Stress flows around every hole in the skin and piles up at tight corners. After about a thousand flights, the metal cracked.
So the real lesson wasn't just "make windows round". It was: design every opening for fatigue. So next time someone tells you...
### Images
- I1: Close-up of a modern airliner cabin window with rounded corners, clouds outside.
- I2: A 1950s jet airliner in flight: sleek unpainted silver body, unmarked with no airline livery, four engines buried in the wing roots, small rounded-rectangle cabin windows.
- I3: A salvage ship with a crane on a calm sea at dusk.
- I4: An airliner fuselage submerged in a huge indoor water tank, engineers on a gantry above.
- I5: Edit of I4 using it as reference: the same tank scene with the fuselage split open along a jagged crack.
- I6: Top of an aircraft fuselage with two small rectangular antenna cut-outs in the roof, an orange crack spreading from one corner.
- I7: A fuselage section gently swelling and relaxing like a breathing balloon, with curved arrows.
- I8: Macro close-up of a hairline crack growing from the corner of a hole in an aluminium sheet.
- I9: Engineers with a flashlight inspecting the rounded window frames of a modern airliner.
- Clip C1 from I1: clouds drift past outside the window; light shifts gently
### Beats
- You've probably heard plane windows are round because square ones made jets crash. That's only half right. → C1 hook clip; local square-window icon struck through [C1, L]
- In 1954, two de Havilland Comets… broke apart in mid-air… → I2 Comet, then I3 salvage ship [I2, I3]
- Investigators sank an entire Comet fuselage in a giant water tank… → I4 tank; flight-cycle counter ticks up; I5 split [I4, I5, L]
- Wait. → Freeze I2 and grey; lens shows the rounded passenger windows; Mark '?'→'!' [L, M]
- …just tightly rounded… began at the corner of a small antenna window in the roof. → Local window-shape comparison card, then I6 roof cut-outs with a highlight ring [L, I6]
- Every flight, the cabin swells slightly, then relaxes… → I7 breathing fuselage, then local stress-line diagram (sharp vs rounded) [I7, L]
- After about a thousand flights, the metal cracked. → I8 crack macro; counter stops at about 1,000 [I8, L]
- So the real lesson… design every opening for fatigue. So next time someone tells you… → I9 inspection; Mark points; hard loop cut to the hook [I9, M]