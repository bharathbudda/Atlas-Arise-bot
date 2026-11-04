"""Render frames in parallel, mix audio (VO + ducked music bed + SFX), and encode the master.
usage: python3 finish.py ep01 [ep02 ...]"""
import json, subprocess, sys, pathlib, math, re, shutil
ED = pathlib.Path(__file__).resolve().parent
ROOT = ED.parent
SFX = {n: str(ROOT / "sample10" / f"sfx_{n}.wav") for n in ("hit", "whoosh", "pop", "tape", "scribble")}
MUSIC = str(ROOT / "prod" / "music" / "music_A.mp3")
OUT = ROOT / "out"; OUT.mkdir(exist_ok=True)
WORKERS = 4

def run(cmd, **kw): return subprocess.run(cmd, check=True, **kw)

def render(ep):
    tl = json.load(open(ED / "build" / ep / "timeline.json"))
    n = math.ceil(tl["total"] * 30)
    fdir = ED / "build" / ep / "frames"
    if fdir.exists(): shutil.rmtree(fdir)
    step = math.ceil(n / WORKERS)
    procs = [subprocess.Popen(["node", str(ED / "render.cjs"), ep, str(a), str(min(n, a + step))]) for a in range(0, n, step)]
    for p in procs:
        if p.wait() != 0: raise SystemExit(f"render failed for {ep}")
    return n

def mix(ep):
    tl = json.load(open(ED / "build" / ep / "timeline.json")); total = tl["total"]
    d = ED / "build" / ep
    inputs = ["-i", str(d / "vo.wav"), "-stream_loop", "-1", "-i", MUSIC]
    filt = [f"[1]atrim=0:{total},afade=t=in:d=0.6,afade=t=out:st={total-1.0}:d=1.0,volume=0.22,aresample=48000[mus]",
            "[0]asplit=2[vo][key]",
            "[mus][key]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[duck]"]
    labels = ["[vo]", "[duck]"]
    for k, (t, name, vol) in enumerate(tl["sfx"]):
        inputs += ["-i", SFX[name]]; ms = int(t * 1000)
        filt.append(f"[{k+2}]adelay={ms}|{ms},volume={vol},aresample=48000[s{k}]"); labels.append(f"[s{k}]")
    filt.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0,apad=whole_dur={total},atrim=0:{total}[pre]")
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt), "-map", "[pre]", "-ac", "2", "-ar", "48000", str(d / "pre.wav")])
    # two-pass loudness: measure, then gain + true-peak limiter to -14 LUFS / -1 dBTP
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(d / "pre.wav"), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    js = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}:"
          f"measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true,alimiter=limit=0.84:level=disabled,aresample=48000")
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(d / "pre.wav"), "-af", af, str(d / "mix.wav")])

def encode(ep, title):
    d = ED / "build" / ep
    out = OUT / f"WTF_{ep.upper()}_{title}.mp4"
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-framerate", "30", "-i", str(d / "frames" / "%05d.jpg"), "-i", str(d / "mix.wav"),
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", "-maxrate", "16M", "-bufsize", "24M",
         "-movflags", "+faststart", "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-shortest", str(out)])
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(out), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    I = re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1]; P = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1]
    dur = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)]).decode().strip()
    print(f"{out.name}: {float(dur):.2f}s, {I} LUFS, peak {P} dBFS")
    return out

TITLES = {"ep01": "GPS_Einstein", "ep02": "Whale_Hippo", "ep03": "Twelve_Notes", "ep04": "Bacteria_Myth", "ep05": "OK_Joke", "ep06": "Plane_Windows"}
if __name__ == "__main__":
    for ep in sys.argv[1:]:
        n = render(ep); print(ep, "frames", n, flush=True)
        mix(ep); encode(ep, TITLES[ep])
