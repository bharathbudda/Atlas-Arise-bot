"""Builds each episode's render timeline (shots, lens, Mark, anchor, captions, SFX cues) from the
recorded VO timings, so every cut lands on the real voice."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent
B = ROOT / "build"
M = "build/media"  # relative to edit/engine.html

def T(ep):
    tm = json.load(open(B / ep / "timing.json"))
    return tm, {l["i"]: l for l in tm["lines"]}

def at(L, i, f=0.0):
    l = L[i]; return round(l["start"] + (l["end"] - l["start"]) * f, 3)

# ---------- captions: 1–3 word chunks, timed by character share within each line
SMALL = {'a','an','the','of','to','in','on','at','and','is','are','from','for','by','with','that','its','it','your','you','so','but','or','as','into','than'}
def chunks(text):
    words = [w for w in text.replace("…", "...").split(" ") if w]
    out, cur = [], []
    for w in words:
        cur.append(w)
        joined = " ".join(cur)
        end = re.search(r"[.?!:;,]$", w)
        small = w.lower().strip('"') in SMALL
        if end or ((len(cur) >= 3 or len(joined) >= 15) and not small):
            out.append(joined); cur = []
    if cur: out.append(" ".join(cur))
    return out

DISPLAY = [("twenty thousand kilometres","20,000 km"),("forty-five microseconds","45 µs"),("four kilometres a second","4 km a second"),
 ("seven microseconds","7 µs"),("thirty-eight microseconds","38 µs"),("ten kilometres","10 km"),("fifty million","50 million"),
 ("twenty-two shrutis","22 shrutis"),("five or seven tones","5 or 7 tones"),("seven octaves","7 octaves"),("thirty-eight trillion","38 trillion"),
 ("thirty trillion","30 trillion"),("eighty-four percent","84%"),
 ("two hundred grams","200 grams"),("Ten microbes","10 microbes"),("forty years","40 years"),("the twenty-third of March, 1839","23\u00a0March\u00a01839"),("one point three to one","1.3\u00a0to\u00a01"),("ten to one","10\u00a0to\u00a01"),("O.K. Clubs","O.K.\u00a0Clubs"),("the Pythagorean comma","the Pythagorean\u00a0comma")]
def display(t):
    for a, b in DISPLAY: t = t.replace(a, b)
    t = re.sub(r"(\d) (km|µs|million|trillion|grams|or|to|March)\b", lambda m: m.group(1) + "\u00a0" + m.group(2), t)
    return t

def caps_for(L, emph, skip=(), big=()):
    caps = []
    for i, l in L.items():
        if i in skip: continue
        txt = display(l["text"])
        if i in big:  # standalone Wait. lines
            caps.append({"t0": l["start"], "t1": l["end"] + 0.45, "html": f"<span>{txt}</span>", "top": big[i], "size": 190}); continue
        cs = chunks(txt); total = sum(len(c) for c in cs); t = l["start"]; dur = l["end"] - l["start"]
        for c in cs:
            d = dur * len(c) / total
            h = c
            for e in emph:
                h = re.sub(r"(?i)\b(" + re.escape(e).replace("\\ ", "[ \u00a0]") + r")(?!\w)", r"<em>\1</em>", h)
            caps.append({"t0": round(t, 3), "t1": round(t + d, 3), "html": h})
            t += d
    return caps

def still(src, t0, t1, **mv):
    return {"type": "still", "src": f"{M}/{src}.jpg", "t0": t0, "t1": t1, "move": mv or {"s0": 1.0, "s1": 1.07}}
def clip(ep, t0, t1, **mv):
    return {"type": "clip", "dir": f"{M}/{ep}_C1", "nframes": 151, "t0": t0, "t1": t1, "move": mv or {"s0": 1.0, "s1": 1.08}}
def card(kind, t0, t1, **kw):
    return {"type": "card", "t0": t0, "t1": t1, "card": {"kind": kind, **kw}}
def freeze(src, t0, t1, lens):
    return {"type": "freeze", "src": src, "t0": t0, "t1": t1, "move": {"s0": 1.0, "s1": 1.0}, "lens": lens}

def flipmark(t0, t1, x=30, y=1420, h=420, pose="neutral"):
    return {"t0": t0 + 0.35, "t1": t1, "pose": pose, "x": x, "y": y, "h": h, "enter": "pop", "flip": round(t0 + 0.85, 3)}

LENS_TXT = lambda big, small: (f"<div style='position:absolute;inset:0;background:#fff;display:grid;place-content:center;text-align:center'>"
    f"<div style='font:700 120px/1 JB;color:#13213C'>{big}</div><div style='font:700 52px CV;color:#E0700A;margin-top:10px'>{small}</div></div>")

def ep01():
    tm, L = T("ep01"); e = "ep01"
    shots = [clip(e, 0, at(L,2)),
             still("ep01_I2", at(L,2), at(L,2,.48)), still("ep01_I3", at(L,2,.48), at(L,3), s0=1.04, s1=1.12),
             still("ep01_I4", at(L,3), at(L,4)), still("ep01_I5", at(L,4), at(L,5), x0=-20, x1=20),
             card("bars", at(L,5), at(L,6), title="satellite clock, per day", max=48, unit="microseconds per day", src="ASHBY 2002",
                  items=[{"label":"GRAVITY","v":45,"valtext":"+45"},{"label":"SPEED","v":-7,"valtext":"−7","color":"#6F84A8"},{"label":"NET","v":38,"valtext":"+38","dash":True}]),
             freeze(f"{M}/ep01_I5.jpg", at(L,6), at(L,7), {"cx":560,"cy":1180,"r":300,"html":LENS_TXT("≈ 11 km","of error, per day")}),
             still("ep01_I6", at(L,7), at(L,7,.42)), card("errorbar", at(L,7,.42), at(L,8)),
             still("ep01_I7", at(L,8), at(L,9)), still("ep01_I8", at(L,9), tm["total"], s0=1.0, s1=1.1)]
    mark = [{"t0": at(L,1,.6), "t1": at(L,2,.1), "pose":"peek","x":700,"y":1380,"h":430,"enter":"slide"},
            {"t0": at(L,5,.45), "t1": at(L,6), "pose":"shrug","x":640,"y":1420,"h":380,"enter":"pop"},
            flipmark(at(L,6), at(L,7,.05))]
    anchor = {"label":"SATELLITE CLOCK","hideOnCard":True,"values":[[at(L,3,.7),"+45 µs/day"],[at(L,4,.8),"+38 µs/day"],[at(L,8,.6),"tuned ✓"]]}
    caps = caps_for(L, ["wrong","purpose","timing","faster","slower","38 µs","10 km","slow","blue dot","speed of light"], big={6:280})
    return dict(badge=["FACT 01","TECH"], shots=shots, mark=mark, anchor=anchor, caps=caps, total=tm["total"])

def ep02():
    tm, L = T("ep02"); e = "ep02"
    shots = [clip(e, 0, at(L,2)),
             freeze(f"{M}/ep02_C1/f0121.jpg", at(L,2), at(L,3), {"cx":600,"cy":1250,"r":320,"mag":1.15}),
             card("tree", at(L,3), at(L,4), ring=True),
             still("ep02_I3", at(L,4), at(L,4,.42), y0=30, y1=-30), card("dna", at(L,4,.42), at(L,5)),
             still("ep02_I4", at(L,5), at(L,6), s0=1.0, s1=1.12),
             still("ep02_I5", at(L,6), at(L,6,.5)), card("ankle", at(L,6,.5), at(L,7)),
             still("ep02_I6", at(L,7), at(L,7,.55)), still("ep02_I7", at(L,7,.55), at(L,8)),
             still("lt_3_gpt_hippo", at(L,8), tm["total"], s0=1.0, s1=1.1)]
    mark = [flipmark(at(L,2), at(L,3,.05)),
            {"t0": at(L,3,.35), "t1": at(L,4), "pose":"point","x":690,"y":1400,"h":360,"enter":"slide","mirror":True},
            {"t0": at(L,5,.3), "t1": at(L,6), "pose":"think","x":680,"y":1390,"h":400,"enter":"pop"},
            {"t0": at(L,8,.3), "t1": tm["total"], "pose":"peek","x":700,"y":1380,"h":430,"enter":"slide"}]
    anchor = {"label":"EVIDENCE","hideOnCard":True,"values":[[at(L,4,.5),"DNA ✓"],[at(L,6,.6),"DNA ✓ fossils ✓"]]}
    caps = caps_for(L, ["hippo","ancestry","DNA","jumping genes","exact same","chance","fossils","double-pulley","cousins","50 million","ocean"], big={2:280})
    return dict(badge=["FACT 02","EVOLUTION"], shots=shots, mark=mark, anchor=anchor, caps=caps, total=tm["total"])

def ep03():
    tm, L = T("ep03")
    shots = [still("ep03_I1", 0, at(L,3), s0=1.0, s1=1.14),
             still("ep03_I3", at(L,3), at(L,3,.3)), card("wave", at(L,3,.3), at(L,3,.64), ratio=[1,2], label="octave: double the frequency"),
             card("wave", at(L,3,.64), at(L,4), ratio=[2,3], label="fifth: times three over two"),
             still("ep03_I4", at(L,4), at(L,5), s0=1.05, s1=1.12, y0=-60, y1=60, origin="50% 20%"),
             freeze(f"{M}/ep03_I4.jpg", at(L,5), at(L,6), {"cx":600,"cy":560,"r":270,"tx":632,"ty":120,"mag":1.9}),
             card("bars", at(L,6), at(L,6,.58), title="12 fifths vs 7 octaves", max=135, unit="times the starting frequency",
                  items=[{"label":"12 FIFTHS","v":129.7,"valtext":"129.7"},{"label":"7 OCTAVES","v":128,"valtext":"128","color":"#6F84A8"}]),
             card("bignum", at(L,6,.58), at(L,7), label="THE PYTHAGOREAN COMMA", num="≈23.5", size=150, sub="cents left over"),
             still("ep03_I5", at(L,7), at(L,7,.45)), card("circle12", at(L,7,.45), at(L,8)),
             still("ep03_I6", at(L,8), at(L,8,.5)), still("ep03_I7", at(L,8,.5), at(L,9)),
             still("ep03_I8", at(L,9), tm["total"])]
    mark = [{"t0": at(L,1,.55), "t1": at(L,3,.1), "pose":"think","x":680,"y":1390,"h":400,"enter":"pop"},
            flipmark(at(L,5), at(L,6,.05)),
            {"t0": at(L,9,.2), "t1": tm["total"], "pose":"thumbs","x":680,"y":1400,"h":400,"enter":"pop"}]
    anchor = {"label":"OCTAVE","hideOnCard":True,"values":[[0.4,"12 keys"],[at(L,4,.6),"12 fifths ≈ 7 octaves"]]}
    caps = caps_for(L, ["twelve","simple ratios","octave","fifth","almost","129.7","128","Pythagorean comma","compromise","not universal","shrutis","gamelan","best deal"], big={5:1380})
    return dict(badge=["FACT 03","MUSIC"], shots=shots, mark=mark, anchor=anchor, caps=caps, total=tm["total"])

def ep04():
    tm, L = T("ep04"); e = "ep04"
    shots = [clip(e, 0, at(L,1,.58)), card("strike", at(L,1,.58), at(L,2), text="10 : 1", after="…says who?"),
             still("ep04_I2", at(L,2), at(L,3)),
             still("ep04_I3", at(L,3), at(L,3,.27)), still("ep04_I4", at(L,3,.27), at(L,3,.55)),
             still("ep04_I5", at(L,3,.55), at(L,3,.78)), card("donut", at(L,3,.78), at(L,4), pct=84, title="your own cells", label="red blood cells"),
             card("bignum", at(L,4), at(L,5), label="BACTERIA : HUMAN CELLS", num="1.3 : 1", size=150, sub="not 10 : 1", src="SENDER ET AL. 2016"),
             freeze(f"{M}/ep04_I1.jpg", at(L,5), at(L,5,.5), {"cx":560,"cy":1100,"r":320,"src":f"{M}/ep04_I6.jpg","tx":560,"ty":1000,"mag":0.95}),
             still("ep04_I6", at(L,5,.5), at(L,6)),
             still("ep04_I4", at(L,6), at(L,7), s0=1.1, s1=1.0),
             still("ep04_I8", at(L,7), tm["total"])]
    mark = [{"t0": at(L,2,.45), "t1": at(L,3), "pose":"facepalm","x":680,"y":1390,"h":400,"enter":"pop"},
            flipmark(at(L,5), at(L,5,.5)),
            {"t0": at(L,7,.25), "t1": tm["total"], "pose":"thumbs","x":680,"y":1400,"h":400,"enter":"pop"}]
    anchor = {"label":"BACTERIA vs YOU","hideOnCard":True,"values":[[at(L,3,.45),"38 trillion vs 30 trillion"],[at(L,6,.7),"toilet trip: can tip to you"]]}
    caps = caps_for(L, ["bacteria","10","1972","40 years","38 trillion","30 trillion","red blood cells","1.3","tiny","200 grams","mango","toilet","tie","overwhelmingly you"], big={})
    for c in caps:  # the Wait line here is long: put its first chunk up top
        if c["html"].startswith("Wait"): c["top"] = 280; c["size"] = 150
    return dict(badge=["FACT 04","BIOLOGY"], shots=shots, mark=mark, anchor=anchor, caps=caps, total=tm["total"])

BUBBLE = ("<div style='position:absolute;left:300px;top:560px;background:#FF8C1A;border:6px solid #13213C;border-radius:40px 40px 40px 8px;"
          "padding:18px 46px;font:800 110px BG;color:#13213C'>ok</div>")
def ep05():
    tm, L = T("ep05"); e = "ep05"
    news = ("<div style='position:absolute;inset:0;background:#F3E7CC'><div style='position:absolute;left:60px;right:60px;top:200px'>"
            + "".join(f"<div style='height:14px;margin:16px 0;background:#B9A98A;width:{70+(i*29)%28}%;border-radius:3px'></div>" for i in range(5))
            + "<div style='font:700 72px Times New Roman,serif;color:#13213C;background:linear-gradient(transparent 55%,#FFB25E 55%);display:inline-block;padding:0 8px'>o.k. — all correct</div>"
            + "".join(f"<div style='height:14px;margin:16px 0;background:#B9A98A;width:{60+(i*37)%35}%;border-radius:3px'></div>" for i in range(6)) + "</div></div>")
    shots = [clip(e, 0, at(L,2)),
             still("ep05_I2", at(L,2), at(L,2,.42)), card("flip", at(L,2,.42), at(L,3), cards=[["O.W.","“oll wright”"],["K.G.","“know go”"]]),
             card("newspaper", at(L,3), at(L,4)),
             still("ep05_I4", at(L,4), at(L,5)),
             still("ep05_I5", at(L,5), at(L,5,.42)), still("ep05_I6", at(L,5,.42), at(L,5,.75)),
             card("bignum", at(L,5,.75), at(L,6), label="1840 · RE-ELECTION CAMPAIGN", num="O.K.", size=200, sub="O.K. Clubs"),
             card("scoreboard", at(L,6), at(L,7), title="1840 result", rows=[["Van Buren","lost",False],["OK","won",True]]),
             freeze(f"{M}/ep05_I2.jpg", at(L,7), at(L,7,.32), {"cx":560,"cy":1150,"r":320,"html":news}),
             still("ep05_I7", at(L,7,.32), at(L,8)),
             dict(still("ep05_I8", at(L,8), tm["total"]), overlay=BUBBLE, overlayAt=0.4)]
    mark = [{"t0": at(L,1,.45), "t1": at(L,2,.1), "pose":"thumbs","x":680,"y":1400,"h":400,"enter":"pop"},
            {"t0": at(L,6,.3), "t1": at(L,7), "pose":"shrug","x":640,"y":1440,"h":360,"enter":"pop"},
            flipmark(at(L,7), at(L,7,.32))]
    anchor = {"label":"YEAR","hideOnCard":True,"values":[[at(L,2),"1838"],[at(L,3),"1839"],[at(L,5),"1840"],[at(L,7,.35),"1963"]]}
    caps = caps_for(L, ["joke","craze","misspelled","oll korrect","all correct","lucky","Old Kinderhook","O.K. Clubs","lost","won","1960s","Allen Walker Read","1839"], big={})
    for c in caps:
        if c["html"].startswith("Wait"): c["top"] = 280; c["size"] = 150
    return dict(badge=["FACT 05","LANGUAGE"], shots=shots, mark=mark, anchor=anchor, caps=caps, total=tm["total"])

RING = "<div style='position:absolute;left:560px;top:880px;width:170px;height:170px;border:12px solid #FF8C1A;border-radius:50%;box-shadow:0 0 0 5px #13213C'></div>"
WIN = ("<div style='position:absolute;inset:0;background:#9CC3E6;display:grid;place-content:center'>"
       "<div style='width:240px;height:330px;border:12px solid #13213C;border-radius:20px;background:#DCEBF7'></div>"
       "<div style='font:700 46px CV;color:#E0700A;text-align:center;margin-top:12px'>already rounded</div></div>")
def ep06():
    tm, L = T("ep06"); e = "ep06"
    shots = [clip(e, 0, at(L,1,.55)), card("squarex", at(L,1,.55), at(L,2)),
             still("ep06_I2", at(L,2), at(L,2,.55), x0=40, x1=-40), still("ep06_I3", at(L,2,.55), at(L,3)),
             still("ep06_I4", at(L,3), at(L,3,.6)), still("ep06_I5", at(L,3,.6), at(L,4)),
             freeze(f"{M}/ep06_I2.jpg", at(L,4), at(L,5), {"cx":560,"cy":1120,"r":300,"html":WIN}),
             card("windows", at(L,5), at(L,5,.45)), dict(still("ep06_I6", at(L,5,.45), at(L,6)), overlay=RING, overlayAt=0.3),
             still("ep06_I7", at(L,6), at(L,6,.3)), card("stress", at(L,6,.3), at(L,6,.76)), still("ep06_I8", at(L,6,.76), at(L,7)),
             still("ep06_I9", at(L,7), tm["total"])]
    mark = [flipmark(at(L,4), at(L,5,.05)),
            {"t0": at(L,7,.35), "t1": tm["total"], "pose":"point","x":40,"y":1410,"h":380,"enter":"slide"}]
    anchor = {"label":"FLIGHT CYCLES","hideOnCard":True,"values":[[at(L,6,.78),"≈ 900–1,300"]]}
    caps = caps_for(L, ["half right","Comets","first jet airliners","water tank","split open","rounded corners","tightly","antenna window","swells","tight corners","thousand","fatigue"], big={4:280})
    return dict(badge=["FACT 06","ENGINEERING"], shots=shots, mark=mark, anchor=anchor, caps=caps, total=tm["total"])

def sfx(tl):
    cues = []
    for s in tl["shots"]:
        if s["type"] == "freeze": cues += [(s["t0"], "hit", 0.55), (s["t0"] + 0.2, "whoosh", 0.35)]
        if s["type"] == "card": cues += [(s["t0"] + 0.22, "tape", 0.4)] + ([(s["t0"] + 0.35, "scribble", 0.22)] if s["card"]["kind"] in ("bars","tree","dna","ankle","stress","windows","wave","errorbar") else [])
    for m in tl["mark"]:
        cues.append((m["t0"], "pop", 0.32))
        if m.get("flip"): cues.append((m["flip"], "pop", 0.45))
    return sorted(cues)

if __name__ == "__main__":
    for ep, fn in [("ep01",ep01),("ep02",ep02),("ep03",ep03),("ep04",ep04),("ep05",ep05),("ep06",ep06)]:
        tl = fn(); tl["sfx"] = sfx(tl)
        json.dump(tl, open(B / ep / "timeline.json", "w"), indent=1)
        print(ep, "shots", len(tl["shots"]), "caps", len(tl["caps"]), "total", tl["total"])
