# WTF Season 1 production plan (review copy)

Credit cap 297.0. Planned 233.65. Retake reserve 53.35. Untouched safety margin 10.

Style block appended to every image prompt:
> Flat 2D editorial explainer illustration in the 'WTF night-notebook' style: clean hand-drawn white chalk outlines with a slight wobble, flat fills in only warm orange (#FF8C1A), dark navy (#13213C) and soft slate blue (#6F84A8), with white highlights and a subtle chalk grain. Solid flat dark navy background (#13213C), no grid. One clear subject with bold, simple shapes and generous empty space, centred in a vertical 9:16 frame with the top 15% and bottom 30% left empty. No text, letters, numbers, logos or watermark. No photorealism, 3D, gradients or drop shadows.

Motion block appended to every clip prompt:
> Animate this exact illustration. Keep the art style, line work, colours and composition identical: flat 2D, chalk outlines, navy background. Smooth, gentle motion only; no camera shake, no new objects, no text, no morphing of the main subject.

## Budget
- P0 | Style lock: 2 test subjects × (GPT Image 2.5 high 1K ×2 @1.5 + Nano Banana Pro 2K ×2 @2.0) | 14.0
- P0 | Motion test: the same start frame on Seedance 2.0 Mini 720p 5 s @5.0 and Kling 3.0 Pro 5 s silent @8.75 | 13.75
- P0 | Voice test: Ainsley sign-off line, ElevenLabs v4 (0.23) ×2 | 0.46
- P0 | Brand music bed: ElevenLabs Music v2.5, 60 s instrumental, 2 takes @8.72 | 17.44
- P1 | Images: 49 (37 stills + 12 clip start frames), priced at the dearer model, Nano Banana Pro 2K @2.0 | 98.0
- P2 | Hero clips: 12 (2 per episode), Seedance 2.0 Mini 720p 5 s silent @5.0 | 60.0
- P3 | Voiceover: Ainsley, ElevenLabs v4, read by paragraph. Quoted 0.69 for 125 chars and 3.22 for 700 chars, so about 5 per episode | 30.0

## EP01 Your phone's map only works because Einstein was right (TECH), 136 words, ≈53s at 155 wpm
### Script
Your phone's blue dot depends on Einstein being right.
GPS is a timing machine. Satellites twenty thousand kilometres up broadcast the exact time, and your phone works out where you are from how long each signal took to arrive.
Up there, gravity is weaker, and relativity says clocks run faster in weaker gravity. About forty-five microseconds a day faster.
But the satellites also move at nearly four kilometres a second, and moving clocks run slow. About seven microseconds slower.
Net result: thirty-eight microseconds fast, every day. Sounds tiny. But the signals travel at the speed of light, so that drift is worth more than ten kilometres of error. Per day.
So engineers tune the clocks to tick slightly slow before launch.
Every time that dot finds you, relativity quietly passes another test.
Wait… that's a fact.
### Verified facts
- GPS satellite clocks gain ~38 µs/day net: about +45.7 µs from weaker gravity (general relativity) and about −7.1 µs from orbital speed (special relativity). [Ashby, Physics Today 2002]
- Uncorrected, one day's drift equals more than 11 km of ranging error (38 µs × speed of light ≈ 11.4 km). [Ashby, Physics Today 2002]
- Satellite clocks are pre-set before launch to 10.22999999543 MHz instead of 10.23 MHz so that they tick correctly once in orbit. [ICD-GPS-200; Penn State GEOG 862]
- Orbit altitude about 20,200 km; orbital speed about 3.9 km/s. [gps.gov]
### Must avoid
- Do not say 'your phone corrects for relativity'. The satellite clocks are offset before launch.
- Do not present '10 km/day' as an exact position drift. Say 'more than ten kilometres of error'.
### Shots
- 0–3.5s | AI clip C1 (start frame S1) | Earth seen from space with one GPS satellite on a dashed orbit; thin signal arcs reach a small orange map pin on the globe. | motion: the satellite glides along the dashed orbit; signal rings pulse toward the pin
- 3.5–8s | AI still S2 | A hand holding a smartphone showing a simple abstract map (shapes only, no labels) with one glowing slate-blue location dot.
- 8–15s | AI still S3 | Four satellites spaced around Earth, dashed lines converging on one point on the surface. (Local animated signal lines on top.)
- 15–20.5s | AI clip C2 (start frame S4) | A round clock floating above Earth; beneath Earth a curved spacetime grid dips like a stretched sheet. Clock face has no numerals. | motion: the curved grid gently ripples outward and the clock hands sweep slightly faster
- 20.5–22.8s | LOCAL diagram D1a | The +45 µs bar (gravity) draws on.
- 22.8–29s | AI still S5 | A GPS satellite streaking past with speed lines behind it, a small clock mounted on its body. Clock face has no numerals.
- 29–34s | LOCAL diagram D1 | −7 µs (speed) bar, then the dashed +38 µs net bar.
- 34–38s | AI still S6 | A thin beam of light racing from a satellite down to Earth, with motion streaks.
- 38–42.6s | LOCAL diagram D2 | Ranging-error bar growing past 10 km: 38 µs × speed of light ≈ 11 km. No map drift.
- 42.6–46.8s | AI still S7 | An engineer's gloved hand turning a tiny dial on a satellite clock in a clean room, a rocket silhouette behind. Clock face has no numerals.
- 46.8–51.1s | AI still S8 | A person walking down a city street at dusk looking at a phone, a glowing slate-blue dot trail behind them.
- 51.1–53.6s | LOCAL end card | The sign-off line plays over the end card, which holds 1 s after the line.

## EP02 A whale's closest living relative is a hippo (EVOLUTION), 146 words, ≈57s at 155 wpm
### Script
A whale's closest living relative is a hippo.
Not a shark. Not a seal. A hippo.
Family trees aren't built on looks, though. They're built on ancestry.
The clincher came from DNA. In 1999, a team in Japan found "jumping genes", bits of DNA that paste copies of themselves into the genome, sitting in the exact same spots in whales and hippos, but not in cows or deer. Insertions like that almost never land in the same place twice by chance.
Then the fossils agreed. In 2001, ancient whales that still had legs turned up with a double-pulley ankle bone, the signature of even-toed hoofed mammals, the group that includes hippos.
Whales didn't evolve from hippos. They share an ancestor that lived more than fifty million years ago.
So that hippo in the river? It's a whale's cousin that kept its legs.
Wait… that's a fact.
### Verified facts
- Retrotransposon (SINE/LINE) insertions shared at the same loci group hippos with cetaceans and exclude ruminants. [Nikaido, Rooney & Okada 1999, PNAS 96:10261]
- 2001 fossils of early legged whales (pakicetids; Rodhocetus, Artiocetus) show the double-pulley astragalus diagnostic of artiodactyls. [Thewissen et al. 2001, Nature 413:277; Gingerich et al. 2001, Science 293:2239]
- Whales and hippos share an ancestor that lived roughly 50–60 million years ago; hippo fossils only reach back about 20 million years. [Boisserie et al. 2005, PNAS]
### Must avoid
- Never say whales evolved from hippos.
- Keep the word 'living'. The closest extinct relatives are raoellids such as Indohyus.
### Shots
- 0–3.1s | AI clip C1 (start frame S1) | Split scene: a hippo standing in a river on the left, a whale breaching from the ocean on the right, a shoreline between them. | motion: the whale rises and splashes back; the hippo flicks its ears and blinks
- 3.1–5.4s | AI still S2 | A shark and a seal side by side, looking puzzled. (Local orange strike-through on each.)
- 5.4–10.5s | AI still S3 | A hand-drawn tree of life branching upward, small generic animal silhouettes at the branch tips.
- 10.5–15.5s | AI clip C2 (start frame S4) | A DNA double helix with small orange segments hovering beside it. | motion: the orange segments hop into slots in the helix one by one
- 15.5–22s | LOCAL diagram D1 | Three DNA strips labelled whale, hippo, cow/deer: an orange insert at the same spot in whale and hippo and missing in cow/deer.
- 22–26.3s | LOCAL diagram D2 | Cladogram as successive branches: (whales + hippos), then cows/deer, then pigs, then camels. Orange marks on the shared branch.
- 26.3–31.4s | AI still S5 | Two darts stuck in exactly the same tiny spot on a plain dartboard with no numbers on the rim.
- 31.4–37s | AI still S6 | Fossil skeleton of a small, wolf-sized, four-legged early whale embedded in layered rock.
- 37–43s | LOCAL diagram D3 | Simplified ankle bone with its two pulley grooves highlighted in orange.
- 43–49.5s | AI still S7 | A small hoofed mammal standing at a riverbank at dawn, a faint silhouette, the shared ancestor.
- 49.5–55s | AI still S8 | A hippo submerged up to its eyes in a river; its reflection on the water is the silhouette of a whale.
- 55–57.5s | LOCAL end card | The sign-off line over the end card, holding 1 s.

## EP03 Why music has 12 notes (MUSIC), 146 words, ≈57s at 155 wpm
### Script
Why does a piano repeat itself every twelve keys?
Because twelve is where maths and your ears almost agree.
Notes sound good together when their frequencies form simple ratios. Double the frequency and you get the same note, an octave higher. Multiply by three over two and you get a fifth, the smoothest-sounding interval after the octave.
Now stack fifths. After twelve of them, you land almost exactly seven octaves up. Almost. Twelve fifths multiply the frequency by 129.7. Seven octaves give exactly 128. That gap is the Pythagorean comma.
Over centuries, musicians settled on a compromise. Shrink every fifth by a hair, and twelve equal steps fit the octave perfectly.
And it's not universal. Indian music theory describes twenty-two shrutis, and Javanese gamelan uses scales of five or seven tones.
Twelve isn't magic. It's the best deal our ears would accept.
Wait… that's a fact.
### Verified facts
- (3/2)^12 ≈ 129.746 versus 2^7 = 128. The gap is the Pythagorean comma, about 23.46 cents. [Calculated; standard tuning theory]
- A pure fifth is 701.955 cents; the 12-TET fifth is 700 cents, about 1.96 cents narrower. [Calculated]
- 12-TET was worked out independently by Zhu Zaiyu (1584) and Simon Stevin (about 1585). [Needham, Science and Civilisation in China, vol. 4]
- Other systems: Indian theory has 22 shrutis; Javanese gamelan uses slendro (5 tones) and pelog (7 tones). [Standard references]
### Must avoid
- Do not say twelve fifths 'close the circle' exactly.
- Do not credit Pythagoras or Bach with inventing the 12-note or equal-tempered scale.
### Shots
- 0–3.5s | AI clip C1 (start frame S1) | A piano keyboard seen from above showing exactly one octave: 7 white keys and 5 black keys in groups of 2 and 3, glowing orange edges. | motion: the keys press down one after another in a wave, soft light pulsing
- 3.5–7.5s | AI still S2 | A cartoon ear and a pocket calculator (blank display, unlabelled buttons) standing side by side, almost touching.
- 7.5–16s | LOCAL diagram D1 | Waveforms at a 2:1 ratio (octave), with real tones generated locally.
- 16–21.5s | LOCAL diagram D1b | Waveforms at a 3:2 ratio (fifth), with tones.
- 21.5–27s | AI clip C2 (start frame S3) | A spiral staircase of twelve steps winding upward through seven floors, a small orange ball on the bottom step. | motion: the ball hops up the spiral steps and lands slightly past the top floor's edge
- 27–34.5s | LOCAL diagram D2 | Bars: twelve fifths = 129.7, seven octaves = 128, with the gap labelled Pythagorean comma (≈23.5 cents).
- 34.5–38s | AI still S4 | A piano tuner with a tuning lever leaning into an open upright piano, nineteenth-century clothes.
- 38–43.5s | LOCAL diagram D3 | A circle cut into 12 equal slices that closes perfectly (equal temperament).
- 43.5–48s | AI still S5 | A sitar and a tanpura resting on a patterned rug.
- 48–51.5s | AI still S6 | A row of bronze gamelan metallophones with mallets.
- 51.5–55s | AI still S7 | A cartoon ear and a piano keyboard shaking hands.
- 55–57.5s | LOCAL end card | The sign-off line over the end card, holding 1 s.

## EP04 You are not 90% bacteria (BIOLOGY), 147 words, ≈57s at 155 wpm
### Script
You've heard you're more bacteria than human. Ten microbes for every one of your cells.
That number is wrong.
It came from a rough estimate back in 1972, and it got repeated for more than forty years.
In 2016, researchers in Israel and Canada finally made a careful estimate. About thirty-eight trillion bacteria, mostly in your colon. And about thirty trillion human cells.
That's not ten to one. It's roughly one point three to one.
And most of your own cells are red blood cells, about eighty-four percent of them.
Bacteria are tiny, so all of yours together weigh about two hundred grams. Roughly one mango.
The ratio isn't even fixed. A single trip to the toilet can flush out enough gut bacteria to tip the balance back toward you.
So by count, it's close to a tie. By weight, you're overwhelmingly you.
Wait… that's a fact.
### Verified facts
- A 70 kg reference man has about 3.0×10¹³ human cells and about 3.8×10¹³ bacteria, a ratio of about 1.3:1 (±25%). [Sender, Fuchs & Milo 2016, PLoS Biol 14:e1002533]
- Bacterial mass is about 0.2 kg; red blood cells are about 84% of human cells by count. [Sender et al. 2016]
- The 10:1 figure traces to Luckey 1972, a rough estimate. [Sender et al. 2016]
- One defecation removes about 1/4 to 1/3 of colon bacteria, enough to flip the ratio. [Sender et al. 2016]
- The authors were at the Weizmann Institute (Israel) and SickKids, Toronto (Canada). [ScienceDaily, 28 Jan 2016]
### Must avoid
- Never say 'bacteria outnumber us 10 to 1' as a fact, or that we are mostly bacteria by weight.
### Shots
- 0–2.7s | AI clip C1 (start frame S1) | A human silhouette outline filled with hundreds of tiny orange rod- and dot-shaped bacteria. | motion: the bacteria swirl slowly inside the silhouette like a gentle current
- 2.7–7.4s | LOCAL diagram D0 | '10 : 1' stamped, then struck through in orange.
- 7.4–14.3s | AI still S2 | A 1970s desk with a typewriter, a coffee mug, and a blank sheet covered in wavy pencil lines.
- 14.3–19s | AI still S3 | A scientist at a desk with stacks of blank papers and a calculator (blank display, unlabelled buttons).
- 19–24s | AI clip C2 (start frame S4) | A stylised winding intestine tube, friendly and non-gory, filled with tiny orange bacteria. | motion: the bacteria drift slowly along the winding tube
- 24–29s | LOCAL diagram D1 | Bars: 38 trillion bacteria vs 30 trillion human cells, ratio ≈ 1.3 : 1.
- 29–34.8s | LOCAL diagram D2 | Donut chart: red blood cells are 84% of human cells.
- 34.8–41s | AI still S5 | An old balance scale with a single mango on one pan and a small heap of tiny orange bacteria on the other, level.
- 41–45s | AI still S6 | A seesaw with a cartoon human on one end and a cloud of bacteria on the other, perfectly level.
- 45–50.3s | AI still S6b | The same seesaw (edit of S6), now tipped so the human's end is down.
- 50.3–55.4s | AI still S7 | The same human silhouette standing confidently, glowing softly, a few bacteria orbiting around it.
- 55.4–57.9s | LOCAL end card | The sign-off line over the end card, holding 1 s.

## EP05 OK started as a joke (LANGUAGE), 133 words, ≈51s at 155 wpm
### Script
"OK" is one of the most widely understood words on the planet. And it started as a joke.
In the late 1830s, Boston newspapers had a craze for abbreviating deliberately misspelled phrases. O.W. for "oll wright". K.G. for "know go".
On the twenty-third of March, 1839, the Boston Morning Post printed "o.k.", short for "all correct", jokingly spelled "oll korrect".
Most of these jokes died. OK got lucky.
In 1840, President Martin Van Buren ran for re-election. His nickname was "Old Kinderhook", after his hometown. Supporters formed O.K. Clubs, and suddenly two letters were everywhere.
Van Buren lost. The word won.
Nobody pieced this together until the 1960s, when linguist Allen Walker Read dug through old newspapers.
So every time you text "OK", you're finishing a joke from 1839.
Wait… that's a fact.
### Verified facts
- First known print use: Boston Morning Post, 23 March 1839, 'o.k.—all correct—', playing on the misspelling 'oll korrect'. [Allen Walker Read, American Speech 38 (1963); Merriam-Webster]
- It came from an 1838–39 Boston fad of abbreviated misspellings (O.W. 'oll wright', K.G. 'know go'). [Merriam-Webster; Read 1963–64]
- 1840: supporters of Martin Van Buren ('Old Kinderhook') formed O.K. Clubs, which spread the term. Van Buren lost the election. [Read 1963–64; Metcalf, OK (2010)]
### Must avoid
- Do not say OK came FROM 'Old Kinderhook'. The campaign spread it.
- Do not use the debunked origins (Choctaw 'okeh', Wolof, Greek 'ola kala').
### Shots
- 0–4.6s | AI clip C1 (start frame S1) | A vintage hand-operated printing press with a sheet of paper; solid blank areas, no print. | motion: the press lever pulls down and stamps the sheet; a puff of ink dust
- 4.6–7s | AI still S2 | An 1830s Boston street, a newsboy in a cap holding up newspapers with solid blank pages and no print.
- 7–15.5s | LOCAL diagram D1 | Handwritten cards flip: O.W. = 'oll wright', K.G. = 'know go'.
- 15.5–23.2s | AI still S3 | Close-up of an old newspaper page made of solid blank column blocks with no print. Locally overlaid: 'o.k. — all correct' in period type, then 'oll korrect'.
- 23.2–26.3s | AI still S4 | A wastebasket full of crumpled paper with one sheet floating up out of it.
- 26.3–31.3s | AI clip C2 (start frame S5) | An 1840 election rally: top hats, a crowd, banners made of solid blank cloth with no print. | motion: the crowd waves their hats and the blank banners sway
- 31.3–34s | AI still S6 | A generic nineteenth-century American statesman with large sideburns in a dark coat. Not a portrait likeness.
- 34–36.8s | AI still S7 | A single campaign banner of blank cloth on two poles, no print. Locally overlaid: 'O.K.'.
- 36.8–39.1s | LOCAL diagram D2 | A scoreboard: 'Van Buren — lost' and 'OK — won'.
- 39.1–45.3s | AI still S8 | A 1960s linguist in a library among stacks of old newspapers with solid blank pages and no print, holding a magnifying glass.
- 45.3–49.9s | AI still S9 | A modern hand typing on a smartphone with a blank screen. Locally overlaid: a chat bubble reading 'ok'.
- 49.9–52.4s | LOCAL end card | The sign-off line over the end card, holding 1 s.

## EP06 Plane windows: the myth and the real story (ENGINEERING), 146 words, ≈57s at 155 wpm
### Script
You've probably heard plane windows are round because square ones made jets crash. That's only half right.
In 1954, two de Havilland Comets, the world's first jet airliners, broke apart in mid-air, less than three months apart.
Investigators sank an entire Comet fuselage in a giant water tank and pressurised it again and again, flight after simulated flight, until it split open.
Here's the twist. The Comet's passenger windows already had rounded corners, just tightly rounded. The inquiry found the first break-up most likely began at the corner of a small antenna window in the roof.
Every flight, the cabin swells slightly, then relaxes. Stress flows around every hole in the skin and piles up at tight corners. After about a thousand flights, the metal cracked.
So the real lesson wasn't just "make windows round". It was: design every opening for fatigue.
Wait… that's a fact.
### Verified facts
- BOAC 781 (G-ALYP) broke up off Elba on 10 Jan 1954; SAA 201 (G-ALYY) broke up near Naples on 8 Apr 1954. [Cohen Court of Inquiry report, HMSO 1955]
- The inquiry found the break-up most probably began at the corner of the rear ADF (antenna) window in the cabin roof, at a bolt hole, where fatigue was found. [Cohen report, para 77]
- Fundamental cause: stresses around the corners of windows and other cut-outs were too high for a long fatigue life. [Cohen report, para 79]
- The G-ALYU water-tank test failed at a window corner after the equivalent of about 3,060 flights (1,230 real + 1,830 tank cycles). [Cohen report]
- The Comet 1 passenger windows were rectangular with rounded corners. [Cohen report; FAA Lessons Learned]
- G-ALYP had made about 1,290 pressurised flights and G-ALYY about 900 before breaking up. [Cohen report; FAA Lessons Learned]
### Must avoid
- Do not say 'square passenger windows cracked'.
- Say bolt hole, not rivet hole.
- Do not blame punch-riveting (a later, disputed claim).
### Shots
- 0–5s | AI clip C1 (start frame S1) | Close-up of a modern airliner cabin window with rounded corners, clouds outside. | motion: clouds drift past outside the window; light shifts gently
- 5–6.6s | LOCAL diagram D0 | A square window shape struck through, then 'half right'.
- 6.6–10.5s | AI still S2 | A 1950s jet airliner in flight: sleek unpainted silver body, unmarked with no airline livery, four engines buried in the wing roots, rounded-rectangle cabin windows.
- 10.5–14.3s | AI still S3 | A salvage ship with a crane on a calm sea at dusk.
- 14.3–19.3s | AI clip C2 (start frame S4) | An airliner fuselage submerged in a huge indoor water tank, engineers on a gantry above. | motion: the water surface ripples rhythmically as if the fuselage is being pressurised and released
- 19.3–24s | AI still S5 | The same tank scene (edit of S4) with the fuselage split open along a jagged crack.
- 24–29.4s | LOCAL diagram D1 | The Comet passenger window shape: a rectangle with tightly rounded corners, next to a modern window with large-radius corners.
- 29.4–37.2s | AI still S6 | Top of an aircraft fuselage with two small rectangular antenna cut-outs in the roof, an orange crack spreading from one corner. (Local highlight ring.)
- 37.2–40.3s | AI still S7 | A fuselage section gently swelling and relaxing like a breathing balloon, with curved arrows.
- 40.3–45.7s | LOCAL diagram D2 | Stress lines flowing around a sharp-cornered hole (bunched up, orange) versus a rounded hole (smooth).
- 45.7–48.8s | AI still S8 | Macro close-up of a hairline crack growing from the corner of a hole in an aluminium sheet.
- 48.8–55s | AI still S9 | Engineers with a flashlight inspecting the rounded window frames of a modern airliner.
- 55–57.5s | LOCAL end card | The sign-off line over the end card, holding 1 s.