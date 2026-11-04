"""Per episode: trim silence from each VO line, speed up gently, lay lines on a timeline with
designed gaps, and write vo.wav + timing.json (line start/end) for the visual timeline."""
import json, subprocess, pathlib, sys, glob, os

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROD = ROOT / "prod"
OUT = ROOT / "edit" / "build"
TEMPO = float(os.environ.get("TEMPO", "1.06"))
LEAD = 0.12   # silence before the first line
GAP = 0.16    # normal gap between lines
WAIT_PAD = 0.32  # extra air around a standalone "Wait."
TAIL = 0.35   # after the last line (loop cut)

def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))

SKIP = {"ep03": [2]}
TEMPOS = {"ep05": 1.08}

def prep(ep, tempo=None):
    tempo = tempo or TEMPOS.get(ep, TEMPO)
    lines = json.load(open(PROD / "vo" / "lines.json"))[ep]
    keep = [i for i in range(1, len(lines) + 1) if i not in SKIP.get(ep, [])]
    d = OUT / ep; d.mkdir(parents=True, exist_ok=True)
    trimmed = []
    for i in keep:
        src = PROD / "vo" / ep / f"l{i}.mp3"; dst = d / f"t{i}.wav"
        # strip leading/trailing silence, then tempo (pitch-preserving), 48 kHz mono
        af = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse,"
              "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,"
              f"atempo={tempo},aresample=48000")
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(src), "-af", af, "-ac", "1", str(dst)], check=True)
        trimmed.append(dst)
    t = LEAD; timing = []; parts = []
    for k, f in enumerate(trimmed):
        i = keep[k] - 1
        txt = lines[i]
        is_wait = txt.strip().startswith("Wait")
        if is_wait and k > 0: t += WAIT_PAD
        dd = dur(str(f)); timing.append({"i": i + 1, "start": round(t, 3), "end": round(t + dd, 3), "text": txt})
        parts.append((f, t)); t += dd + GAP + ((1.05 if len(txt) < 20 else WAIT_PAD) if is_wait else 0)
    total = round(timing[-1]["end"] + TAIL, 3)
    inputs = []; filt = []
    for k, (f, st) in enumerate(parts):
        inputs += ["-i", str(f)]; ms = int(st * 1000); filt.append(f"[{k}]adelay={ms}|{ms}[a{k}]")
    filt.append("".join(f"[a{k}]" for k in range(len(parts))) + f"amix=inputs={len(parts)}:normalize=0,apad=whole_dur={total},atrim=0:{total}[vo]")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt), "-map", "[vo]", "-ar", "48000", str(d / "vo.wav")], check=True)
    json.dump({"total": total, "tempo": tempo, "lines": timing}, open(d / "timing.json", "w"), indent=1)
    return total

if __name__ == "__main__":
    eps = sys.argv[1:] or ["ep01", "ep02", "ep03", "ep04", "ep05", "ep06"]
    for ep in eps:
        print(ep, prep(ep))
