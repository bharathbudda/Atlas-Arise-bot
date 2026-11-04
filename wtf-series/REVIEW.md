# WTF Season 1 production plan (review copy)

Credit cap 297.0. Planned 231.69. Retake reserve 55.31. Untouched safety margin 10.

Style block appended to every image prompt:
> Flat 2D editorial explainer illustration in the 'WTF night-notebook' style: clean hand-drawn white chalk outlines with a slight wobble, flat fills in only warm orange (#FF8C1A), dark navy (#13213C) and soft slate blue (#6F84A8), with white highlights and a subtle chalk grain. Solid flat dark navy background (#13213C), no grid. One clear subject with bold, simple shapes and generous empty space, centred in a vertical 9:16 frame with the top 15% and bottom 30% left empty. No text, letters, numbers, logos or watermark. No photorealism, 3D, gradients or drop shadows.

Motion block appended to every clip prompt:
> Animate this exact illustration. Keep the art style, line work, colours and composition identical: flat 2D, chalk outlines, navy background. Smooth, gentle motion only; no camera shake, no new objects, no text, no morphing of the main subject.

## Budget
- P0 | Style lock: 2 test subjects × (GPT Image 2.5 high 1K ×2 @1.5 + Nano Banana Pro 2K ×2 @2.0) | 14.0
- P0 | Motion test: same start frame on Seedance 2.0 Mini 720p 5s @5.0 and Kling 3.0 Pro 5s silent @8.75 | 13.75
- P0 | Voice test: Ainsley sign-off line (ElevenLabs v4, ~0.23) ×2 | 0.5
- P0 | Brand music bed: ElevenLabs Music v2.5, 60 s instrumental, 2 takes @8.72 | 17.44
- P1 | Stills: 6 eps × 8 (incl. clip start frames), priced at the dearer model (Nano Banana Pro 2K @2.0) | 96.0
- P2 | Hero clips: 6 eps × 2, Seedance 2.0 Mini 720p 5s silent @5.0 | 60.0
- P3 | Voiceover: Ainsley, ElevenLabs v4, ~840 chars per ep ≈ 4.1 + paragraph-split overhead ≈ 5 each | 30.0

## EP01 Your phone's map only works because Einstein was right (TECH), 137 words, ≈53s at 155 wpm
### Script
Your phone's map only works because Einstein was right.
GPS is a timing machine. Satellites twenty thousand kilometres up broadcast the exact time, and your phone works out where you are from how long each signal took to arrive.
Up there, gravity is weaker, and relativity says clocks run faster in weaker gravity. About forty-five microseconds a day faster.
But the satellites also move at nearly four kilometres a second, and moving clocks run slow. About seven microseconds slower.
Net result: thirty-eight microseconds fast, every day. Sounds tiny. But the signals travel at the speed of light, so that drift is worth more than ten kilometres of error. Per day.
So engineers tune the clocks to tick slightly slow before launch.
Every time the blue dot finds you, relativity quietly passes another test.
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
- 0–3s | AI clip C1 (from S1) | Earth seen from space with one GPS satellite on a dashed orbit; thin signal arcs reach a small orange map pin on the globe. | motion: satellite glides along the dashed orbit; signal rings pulse from satellite toward the pin
- 3–8s | AI still S2 | A hand holding a smartphone showing a simple abstract map with one glowing orange location dot.
- 8–13s | AI still S3 | Four satellites spaced around Earth, dashed lines converging on one point on the surface.
- 13–20s | AI clip C2 (from S4) | A round clock floating above Earth; beneath Earth a curved spacetime grid dips like a stretched sheet. | motion: the curved grid gently ripples outward and the clock hands sweep slightly faster
- 20–26s | AI still S5 | A GPS satellite streaking past with speed lines behind it, a small clock on its body.
- 26–33s | LOCAL diagram D1 | Bar chart: +45 (gravity), −7 (speed), +38 net, in microseconds per day.
- 33–40s | LOCAL diagram D2 | Map with the dot drifting along a growing line: 38 µs × light speed ≈ 11 km.
- 40–46s | AI still S6 | An engineer's hand turning a tiny dial on a satellite clock in a clean room, a rocket silhouette in the background.
- 46–53s | AI still S7 | A person walking down a city street at dusk looking at a phone, a glowing orange dot trail behind them.
- 53–56s | LOCAL end card | Logo flip and the sign-off.

## EP02 A whale's closest living relative is a hippo (EVOLUTION), 146 words, ≈57s at 155 wpm
### Script
A whale's closest living relative is a hippo.
Not a shark. Not a seal. A hippo.
Family trees aren't built on looks, though. They're built on ancestry.
The first big clue came from DNA. In 1999, Japanese scientists found "jumping genes", bits of DNA that paste copies of themselves into the genome, sitting in the exact same spots in whales and hippos, but not in cows or deer. Insertions like that almost never land in the same place twice by chance.
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
- 0–3s | AI clip C1 (from S1) | Split scene: a hippo standing in a river on the left, a whale breaching from the ocean on the right, a shoreline between them. | motion: the whale rises and splashes back; the hippo flicks its ears and blinks
- 3–6s | AI still S2 | A shark and a seal side by side, looking puzzled.
- 6–10s | AI still S3 | A hand-drawn tree of life branching upward, small animal silhouettes at the branch tips.
- 10–22s | AI clip C2 (from S4) | A DNA double helix with small orange segments hovering beside it. | motion: the orange segments hop into matching slots in the helix one by one
- 22–27s | LOCAL diagram D1 | Cladogram: whales + hippos joined, then cows/deer, then pigs and camels, with orange insertion marks on the shared branch.
- 27–35s | AI still S5 | Fossil skeleton of a small, wolf-sized, four-legged early whale embedded in layered rock.
- 35–40s | LOCAL diagram D2 | Simplified ankle bone with two pulley grooves highlighted in orange.
- 40–47s | AI still S6 | A small hoofed mammal standing at a riverbank at dawn, the shared ancestor, its silhouette faint.
- 47–54s | AI still S7 | A hippo submerged up to its eyes in a river; its reflection on the water is the silhouette of a whale.
- 54–57s | LOCAL end card | Logo flip and the sign-off.

## EP03 Why music has 12 notes (MUSIC), 146 words, ≈57s at 155 wpm
### Script
Why does a piano repeat itself every twelve keys? Why not ten?
Because twelve is where maths and your ears almost agree.
Notes sound good together when their frequencies form simple ratios. Double the frequency and you get the same note, an octave higher. Multiply by three over two and you get a fifth, the smoothest-sounding interval after the octave.
Now stack fifths. After twelve of them, you land almost exactly seven octaves up. Almost. The maths gives 129.7 instead of 128. That little gap is called the Pythagorean comma.
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
- 0–3s | AI clip C1 (from S1) | A piano keyboard seen from above, one octave of twelve keys glowing orange. | motion: the twelve keys press down one after another in a wave, soft light pulsing
- 3–8s | AI still S2 | A single string stretched on a wooden board (monochord), a finger plucking it, faint vibration curves.
- 8–20s | LOCAL diagram D1 | Waveforms: ratio 2:1 (octave) and 3:2 (fifth), each with a real tone played (generated locally).
- 20–28s | AI clip C2 (from S3) | A spiral staircase of twelve steps winding upward through seven floors, a small orange ball on the bottom step. | motion: the ball hops up the spiral steps and lands slightly past the top floor's edge
- 28–35s | LOCAL diagram D2 | 129.7 vs 128 bars with the small gap labelled 'Pythagorean comma'.
- 35–41s | AI still S4 | A piano tuner with a tuning lever leaning into an open upright piano, nineteenth-century clothes.
- 41–45s | AI still S5 | A sitar and a tanpura resting on a patterned rug.
- 45–49s | AI still S6 | A row of bronze gamelan metallophones with mallets.
- 49–54s | AI still S7 | A cartoon ear and a piano keyboard shaking hands.
- 54–57s | LOCAL end card | Logo flip and the sign-off.

## EP04 You are not 90% bacteria (BIOLOGY), 147 words, ≈57s at 155 wpm
### Script
You've heard you're more bacteria than human. Ten microbes for every one of your cells.
That number is wrong.
It came from a rough estimate back in 1972, and it got repeated for more than forty years.
In 2016, researchers in Israel and Canada finally did a careful count. About thirty-eight trillion bacteria, mostly in your colon. And about thirty trillion human cells.
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
- 0–3s | AI clip C1 (from S1) | A human silhouette outline filled with hundreds of tiny orange rod- and dot-shaped bacteria. | motion: the bacteria swirl slowly inside the silhouette like a gentle current
- 3–8s | LOCAL diagram D0 | '10 : 1' stamped, then struck through in orange.
- 8–13s | AI still S2 | A 1970s desk with a typewriter, a coffee mug and a sheet of abstract scribbled calculations.
- 13–20s | AI still S3 | A scientist at a microscope, tally marks floating in the air beside them.
- 20–27s | AI clip C2 (from S4) | A stylised winding intestine tube, friendly and non-gory, filled with tiny orange bacteria. | motion: the bacteria drift slowly along the winding tube
- 27–33s | LOCAL diagram D1 | Bars: 38 trillion bacteria vs 30 trillion human cells, ratio ≈ 1.3 : 1.
- 33–37s | LOCAL diagram D2 | Donut chart: red blood cells 84% of human cells.
- 37–43s | AI still S5 | An old balance scale: a single mango on one pan, a small heap of tiny orange bacteria on the other, level.
- 43–49s | AI still S6 | A seesaw with a cartoon human on one end and a cloud of bacteria on the other, the human's side just touching down.
- 49–54s | AI still S7 | The same human silhouette standing confidently, glowing softly, a few bacteria orbiting around it.
- 54–57s | LOCAL end card | Logo flip and the sign-off.

## EP05 OK started as a joke (LANGUAGE), 136 words, ≈53s at 155 wpm
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
- 0–3s | AI clip C1 (from S1) | A vintage hand-operated printing press with a blank newspaper sheet. | motion: the press lever pulls down and stamps the sheet; a puff of ink dust
- 3–9s | AI still S2 | An 1830s Boston street, a newsboy in a cap holding up blank newspapers.
- 9–15s | LOCAL diagram D1 | Handwritten cards flip: O.W. = 'oll wright', K.G. = 'know go'.
- 15–22s | AI still S3 | Close-up of an old newspaper page with blank columns; we overlay 'o.k. — all correct' locally in period type.
- 22–30s | AI clip C2 (from S4) | An 1840 election rally: top hats, a crowd, blank banners on poles. | motion: the crowd waves hats and the blank banners sway
- 30–35s | AI still S5 | A nineteenth-century American statesman with large sideburns in a dark coat, a generic illustration rather than a portrait likeness.
- 35–40s | AI still S6 | A telegraph key with copper wires stretching away across a landscape.
- 40–47s | AI still S7 | A 1960s linguist in a library surrounded by stacks of old newspapers, holding a magnifying glass.
- 47–52s | AI still S8 | A modern hand typing on a smartphone; we overlay a chat bubble saying 'ok' locally.
- 52–55s | LOCAL end card | Logo flip and the sign-off.

## EP06 Plane windows: the myth and the real story (ENGINEERING), 144 words, ≈56s at 155 wpm
### Script
You've probably heard plane windows are round because square ones made jets crash. That's only half right.
In 1954, two de Havilland Comets, the world's first jet airliners, broke apart in mid-air, less than three months apart.
Investigators sank an entire Comet fuselage in a giant water tank and pressurised it again and again, flight after simulated flight, until it split open.
Here's the twist. The Comet's passenger windows already had rounded corners. The inquiry traced the first break-up to a fatigue crack at the corner of a small antenna window in the roof.
Every flight, the cabin swells slightly, then relaxes. Stress flows around every hole in the skin and piles up at tight corners. Thousands of cycles later, the metal cracks.
So the real lesson wasn't just "make windows round". It was: design every opening for fatigue.
Wait… that's a fact.
### Verified facts
- BOAC 781 (G-ALYP) broke up off Elba on 10 Jan 1954; SAA 201 (G-ALYY) broke up near Naples on 8 Apr 1954. [Cohen Court of Inquiry report, HMSO 1955]
- The inquiry found the break-up most probably began at the corner of the rear ADF (antenna) window in the cabin roof, at a bolt hole, where fatigue was found. [Cohen report, para 77]
- Fundamental cause: stresses around the corners of windows and other cut-outs were too high for a long fatigue life. [Cohen report, para 79]
- The G-ALYU water-tank test failed at a window corner after the equivalent of about 3,060 flights (1,230 real + 1,830 tank cycles). [Cohen report]
- The Comet 1 passenger windows were rectangular with rounded corners. [Cohen report; FAA Lessons Learned]
### Must avoid
- Do not say 'square passenger windows cracked'.
- Say bolt hole, not rivet hole.
- Do not blame punch-riveting (a later, disputed claim).
### Shots
- 0–3s | AI clip C1 (from S1) | Close-up of a modern airliner cabin window with rounded corners, clouds outside. | motion: clouds drift past outside the window; light shifts gently
- 3–6s | LOCAL diagram D0 | A square window shape struck through, then a question mark.
- 6–13s | AI still S2 | A 1950s de Havilland Comet jet airliner in flight, engines buried in the wing roots, sleek silver body.
- 13–22s | AI clip C2 (from S3) | An airliner fuselage submerged in a huge indoor water tank, engineers on a gantry above. | motion: the water surface ripples rhythmically as if the fuselage is being pressurised and released
- 22–30s | AI still S4 | Top of an aircraft fuselage with two small rectangular antenna cut-outs in the roof, an orange crack spreading from one corner.
- 30–40s | LOCAL diagram D1 | Stress lines flowing around a sharp-cornered hole (bunched up, orange) versus a rounded hole (smooth).
- 40–46s | AI still S5 | A fuselage section gently swelling and relaxing like a breathing balloon, with curved arrows.
- 46–52s | AI still S6 | Engineers with a flashlight inspecting the rounded window frames of a modern airliner.
- 52–55s | LOCAL end card | Logo flip and the sign-off.