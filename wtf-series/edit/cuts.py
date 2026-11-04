"""Zero-credit extra posts: three quiz cuts (music + SFX, no VO) and a 30 s recap stitched from masters."""
import json, subprocess, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import finish
ED = pathlib.Path(__file__).resolve().parent; B = ED / "build"; M = "build/media"; OUT = ED.parent / "out" / "cuts"; OUT.mkdir(parents=True, exist_ok=True)

def quiz(name, badge, hero, q, opts, answer=None, reveal=0.62, foot="answer tomorrow"):
    total = 12.0
    tl = {"badge": badge, "total": total, "anchor": None,
          "shots": [{"type": "still", "src": f"{M}/{hero}.jpg", "t0": 0, "t1": 2.6, "move": {"s0": 1.0, "s1": 1.1}, "nosplit": True},
                    {"type": "card", "t0": 2.6, "t1": total, "card": {"kind": "quiz", "q": q, "opts": opts, "answer": answer, "reveal": reveal, "foot": foot}}],
          "mark": [{"t0": 0.6, "t1": 2.6, "pose": "think", "x": 680, "y": 1390, "h": 400, "enter": "pop"},
                   {"t0": 3.2, "t1": total, "pose": "shock" if answer is not None else "think", "x": 790, "y": 1060, "h": 300, "enter": "pop"}],
          "caps": [{"t0": 0.2, "t1": 2.6, "html": "Quiz <em>time</em>", "size": 130}]}
    cues = [(0.6, "pop", 0.32), (2.82, "tape", 0.4), (3.2, "pop", 0.3)] + [(2.6 + (total - 2.6) * (0.12 + i * 0.1), "pop", 0.25) for i in range(len(opts))]
    if answer is not None: cues += [(2.6 + (total - 2.6) * reveal, "hit", 0.5)]
    tl["sfx"] = sorted(cues)
    d = B / name; d.mkdir(parents=True, exist_ok=True)
    json.dump(tl, open(d / "timeline.json", "w"), indent=1)
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=mono", "-t", str(total), str(d / "vo.wav")], check=True)
    finish.render(name); finish.mix(name)
    return finish.encode(name, "quiz").rename(OUT / f"{name}.mp4")

def recap():
    """Three 'Wait.' moments from the masters, joined with a title card overlay."""
    parts = []
    for ep, a, b in [("ep02", 1, 3), ("ep01", 5, 7), ("ep06", 4, 5)]:
        tm = json.load(open(B / ep / "timing.json")); L = {l["i"]: l for l in tm["lines"]}
        t0 = max(0, L[a]["start"] - 0.1); t1 = L[b]["end"] + 0.25
        src = next((ED.parent / "out").glob(f"WTF_{ep.upper()}_*.mp4"))
        seg = B / f"recap_{ep}.mp4"
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{t0}", "-to", f"{t1}", "-i", str(src),
                        "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "320k", "-ar", "48000", str(seg)], check=True)
        parts.append(seg)
    lst = B / "recap.txt"; lst.write_text("".join(f"file '{p}'\n" for p in parts))
    font = ED.parent / "brand" / "fonts" / "BricolageGrotesque-ExtraBold.ttf"
    out = OUT / "recap_3facts.mp4"
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-vf", f"drawtext=fontfile={font}:text='3 FACTS · 3 TWISTS':fontsize=64:fontcolor=white:borderw=8:bordercolor=0x13213C:x=(w-tw)/2:y=1560:enable='lt(t,2.5)'",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "320k", "-movflags", "+faststart", str(out)], check=True)
    dur = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)]).decode().strip()
    print(out.name, dur)

if __name__ == "__main__":
    what = sys.argv[1:] or ["quiz", "recap"]
    if "quiz" in what:
        print(quiz("quiz_day03_whale", ["QUIZ", "EVOLUTION"], "ep02_I7", "A whale's closest living relative?", ["Shark", "Seal", "Hippo"]))
        print(quiz("quiz_day06_windows", ["QUIZ", "ENGINEERING"], "ep06_I1", "Why are plane windows rounded?", ["Looks nicer", "Easier to clean", "Metal fatigue"]))
        print(quiz("quiz_day09_bacteria", ["QUIZ", "BIOLOGY"], "ep04_I1", "True or false: you're 90% bacteria", ["True", "False"], answer=1, foot="≈1.3 : 1 · Sender et al. 2016"))
    if "recap" in what:
        recap()
