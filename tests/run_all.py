"""End-to-end tests for the three labs.

Serves the repository with Python's built-in web server, opens each lab in headless
Chromium (desktop light theme and phone dark theme), works through every part as a
student would, and checks the numbers each lab reports against the values the
teaching materials rely on.

    pip install -r tests/requirements.txt
    python -m playwright install chromium
    python tests/run_all.py            # full run, about 4 minutes
    python tests/run_all.py --quick    # skips the 90-second reaction-time task on phone size
"""
import asyncio
import functools
import http.server
import re
import sys
import threading
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
QUICK = "--quick" in sys.argv
FAILURES = []


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAILURES.append(msg)


def num(text, pattern):
    m = re.search(pattern, text)
    return float(m.group(1).replace("−", "-").replace("+", "")) if m else None


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve():
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


async def slider(pg, sel, v):
    await pg.eval_on_selector(sel, "(e,v)=>{e.value=v;e.dispatchEvent(new Event('input'));e.dispatchEvent(new Event('change'))}", str(v))


async def checkfield(pg, fid, value):
    await pg.fill(f"#f_{fid}", str(value))
    await pg.click(f"[data-check={fid}]")
    return "✓" in await pg.inner_text(f"#fb_{fid}")


# ---------------------------------------------------------------- Spike Lab
async def spike_lab(pg, base):
    await pg.goto(base + "/labs/spike-lab/")
    await pg.click("text=Start Part 1")

    async def fire():
        await pg.click("#go")
        await pg.wait_for_function("document.querySelector('#readout').textContent.trim().length>0")
        return await pg.inner_text("#readout")

    # Part 1: threshold, all-or-none
    await slider(pg, "#s", 4)
    check("No spike" in await fire(), "Spike Lab 1: strength 4 gives no spike")
    await slider(pg, "#s", 4.5)
    r = await fire()
    peak_thr = num(r, r"Peak ([+\-−]?[\d.]+)")
    await slider(pg, "#s", 10)
    peak10 = num(await fire(), r"Peak ([+\-−]?[\d.]+)")
    check(peak_thr is not None and abs(peak_thr - 37) <= 3, f"Spike Lab 1: peak at threshold about +37 mV (got {peak_thr})")
    check(peak10 is not None and abs(peak10 - 41) <= 3, f"Spike Lab 1: peak at strength 10 about +41 mV (got {peak10})")
    check(await checkfield(pg, "thr", 4.5), "Spike Lab 1: threshold 4.5 accepted")
    await pg.click("#next")

    # Part 2: doors and blockers
    await slider(pg, "#s", 8)
    t0 = num(await fire(), r"above 0 mV: ([\d.]+)")
    await pg.check("#nab")
    check("No spike" in await fire(), "Spike Lab 2: sodium blocker abolishes the spike")
    await pg.uncheck("#nab"); await pg.check("#kb")
    tk = num(await fire(), r"above 0 mV: ([\d.]+)")
    await pg.uncheck("#kb")
    check(t0 is not None and abs(t0 - 1.2) <= 0.35, f"Spike Lab 2: time above 0 mV about 1.2 ms (got {t0})")
    check(tk is not None and abs(tk - 2.6) <= 0.4, f"Spike Lab 2: with potassium blocker about 2.6 ms (got {tk})")
    await pg.click("#next")

    # Part 3: refractory period
    async def shortest_gap(strength):
        await slider(pg, "#s", strength)
        for g in range(2, 26):
            await slider(pg, "#g", g)
            if "Both pushes" in await fire():
                return g
    g8, g10 = await shortest_gap(8), await shortest_gap(10)
    check(g8 == 13, f"Spike Lab 3: shortest gap at strength 8 is 13 ms (got {g8})")
    check(g10 == 12, f"Spike Lab 3: shortest gap at strength 10 is 12 ms (got {g10})")
    await pg.click("#next")

    # Part 4: rate coding
    rates = []
    for s in [1, 3, 5, 7, 10]:
        await slider(pg, "#s", s)
        rates.append(num(await fire(), r"= ([\d.]+) spikes per second"))
    check(all(a is not None for a in rates) and rates == sorted(rates) and rates[-1] > rates[1],
          f"Spike Lab 4: firing rate rises with strength (got {rates})")
    await pg.click("#next")
    check(await pg.is_visible("#copyline"), "Spike Lab: results page shows the copy line")


# ---------------------------------------------------------------- Relay Lab
async def relay_lab(pg, base):
    await pg.goto(base + "/labs/relay-lab/")
    await pg.click("text=Continue")

    async def unlock(word, wrong=None):
        if wrong:
            await pg.fill("#pw", wrong); await pg.click("text=Unlock")
            check("Not that one" in await pg.inner_text("#pwfb"), "Relay Lab: a wrong password is refused")
        await pg.fill("#pw", word); await pg.click("text=Unlock")
        await pg.wait_for_selector(".bench-head")

    await unlock("  Cheetah ", wrong="myelin")
    # Part 1: the race
    async def race(d, myel, ms=False, squid=False):
        if squid:
            await pg.click("#sq")
        else:
            await slider(pg, "#d", d)
            if await pg.is_checked("#my") != myel: await pg.click("#my")
            if myel and await pg.is_checked("#ms") != ms: await pg.click("#ms")
            await pg.click("#go")
        await pg.wait_for_timeout(3500)
    await race(1, False); await race(12, True); await race(0, False, squid=True); await race(12, True, ms=True)
    rows = await pg.eval_on_selector_all("#tbl tbody tr", "rs=>rs.map(r=>r.innerText)")
    speeds = [num(r, r"([\d.]+) m/s") for r in rows]
    check(speeds == [1.0, 72.0, 22.0, 10.0], f"Relay Lab 1: speeds 1, 72, 22, 10 m/s (got {speeds})")
    for fid, v in [("c", 1.0), ("m12", 72), ("sq", 22), ("ms", 10)]:
        check(await checkfield(pg, fid, v), f"Relay Lab 1: field {fid} = {v} accepted")
    await pg.click("#next")

    # Part 2: adding up
    await unlock("chorus")
    for i in range(6):
        await pg.click(f'[data-step="{i}"]')
    check("All six in order" in await pg.inner_text("#orderfb"), "Relay Lab 2: synapse steps can be ordered")

    async def fire(boxes):
        for k in "ABCD":
            if await pg.is_checked(f'[data-in="{k}"]') != (k in boxes): await pg.click(f'[data-in="{k}"]')
        await pg.click("#fire"); await pg.wait_for_timeout(900)
        return await pg.inner_text("#readout")
    check(abs((num(await fire("A"), r"rise: ([\d.]+) mV") or 0) - 7.2) < 0.3, "Relay Lab 2: one input raises the voltage about 7 mV")
    check("no spike" in await fire("AB"), "Relay Lab 2: two inputs do not fire")
    check("a spike!" in await fire("ABC"), "Relay Lab 2: three inputs fire")
    check("no spike" in await fire("ABCD"), "Relay Lab 2: inhibition vetoes the spike")
    for g, expect in [(7, "a spike!"), (8, "no spike")]:
        await slider(pg, "#g", g); await pg.click("#rep"); await pg.wait_for_timeout(900)
        check(expect in await pg.inner_text("#readout"), f"Relay Lab 2: repeated input {g} ms apart gives '{expect}'")
    await pg.click("#next")

    # Part 3: keys and locks
    await unlock("KEYRING")
    peaks = {}
    for syn in ["nic", "ser"]:
        await pg.check(f"input[name=syn][value={syn}]")
        for dr in ["none", "antag", "block"]:
            await pg.check(f"input[name=drug][value={dr}]"); await pg.click("#go"); await pg.wait_for_timeout(1200)
            peaks[(syn, dr)] = num(await pg.inner_text("#readout"), r"peaks at ([\d.]+)")
    check(peaks[("nic", "none")] == 100 and peaks[("ser", "none")] == 100, "Relay Lab 3: no drug peaks at 100")
    check(peaks[("nic", "antag")] < 30 and peaks[("nic", "block")] > 150, f"Relay Lab 3: antagonist shrinks, blocker enlarges ({peaks})")
    await pg.click("#next")
    check(await pg.is_visible("#copyline"), "Relay Lab: results page shows the copy line")


# ---------------------------------------------------------------- Prediction Lab
async def prediction_lab(pg, base, behaviour):
    await pg.goto(base + "/labs/prediction-lab/")
    await pg.fill("#pw", "banana"); await pg.click("text=Unlock")
    check("Not that one" in await pg.inner_text("#pwfb"), "Prediction Lab: a wrong start password is refused")
    await pg.fill("#pw", " Juice "); await pg.click("text=Unlock")
    await pg.click("text=Start Part 1")

    if behaviour:   # Part 1: 24 real-time trials (about 90 s)
        await pg.click("#press")
        for k in range(24):
            await pg.wait_for_selector("#lamp.on", timeout=5000)
            try:
                await pg.wait_for_selector("#star.on", timeout=1150)
                await pg.wait_for_timeout(150)
            except Exception:
                pass
            await pg.click("#press")
            await pg.wait_for_selector("#lamp.on", state="hidden", timeout=4000)
        res = await pg.inner_text("#p1res")
        check("3 of 3" in res, "Prediction Lab 1: presses on all three no-star trials are counted")
    await pg.click("#next")

    # Part 2: Fig. 1
    async def rec(cond):
        await pg.check(f"input[name=cond][value={cond}]"); await pg.click("#go")
        t = await pg.inner_text("#tbl")
        return [num(t, p) for p in [r"(?m)Resting[^\n]*\s([\d.]+)\s*$", r"(?m)light \(0\.05[^\n]*\s([\d.]+)\s*$", r"(?m)Juice time[^\n]*\s([\d.]+)\s*$"]]
    r0 = await rec("LJ")
    await pg.click("#train"); await pg.wait_for_function("document.querySelector('#ntr').textContent==='150'")
    r1, r2 = await rec("LJ"), await rec("LO")
    check(r0[2] > 14 and r0[1] < 9 and 2 < r0[0] < 9, f"Prediction Lab 2: before learning, burst at the juice only ({r0})")
    check(r1[1] > 12 and r1[2] < 9, f"Prediction Lab 2: after learning, burst moves to the light ({r1})")
    check(r2[2] < 1.5, f"Prediction Lab 2: withheld juice gives a pause ({r2})")
    await pg.click("#next")

    # Part 3: Fig. 3 (deterministic)
    async def scan():
        await pg.click("#go"); out = []
        for k in range(1, 81):
            await slider(pg, "#k", k); out.append(await pg.inner_text("#ro"))
        half = next(i + 1 for i, t in enumerate(out) if "withheld" not in t and num(t, r"at juice time ([+\-\d.]+)") < 0.5)
        trans = next(i + 1 for i, t in enumerate(out) if "withheld" not in t and "biggest positive response at 0.0 s" in t)
        return half, trans
    check(await scan() == (3, 26), "Prediction Lab 3: timing learned by trial 3, transfer to the light by trial 26")
    await pg.check("#bl")
    check(await scan() == (6, 49), "Prediction Lab 3: with the blocker, trials 6 and 49")
    await pg.click("#next")

    # Part 4: probes
    async def probe(k):
        await pg.check(f"input[name=tst][value={k}]"); await pg.click("#go")
        t = await pg.inner_text("#tbl")
        return {w: num(t, rf"At {w} s\s+([\d.]+)") for w in ["0.0", "0.5", "1.0", "1.5"]}
    late, early, g = await probe("c"), await probe("d"), await probe("g")
    check(late["1.0"] < 1.5 and late["1.5"] > 14, f"Prediction Lab 4: late juice gives a pause then a burst ({late})")
    check(early["0.5"] > 14 and early["1.0"] < 1.5, f"Prediction Lab 4: early juice gives a burst and a pause ({early})")
    check(g["0.5"] < 4.5 and g["1.0"] > 8, f"Prediction Lab 4: light 2 left out gives a dip then a smaller burst ({g})")
    await pg.click("#next")
    check(await pg.is_visible(".copyline"), "Prediction Lab: summary page shows the copy line")


# ---------------------------------------------------------------- landing page
async def landing(browser, base):
    print("Landing page")
    pg = await browser.new_page()
    await pg.route(re.compile(r"https://fonts\.(googleapis|gstatic)\.com/.*"),
                   lambda route: route.fulfill(status=200, body="", content_type="text/css"))
    await pg.goto(base + "/")
    hrefs = await pg.eval_on_selector_all("main a[href]", "as=>as.map(a=>a.getAttribute('href'))")
    local = [h for h in hrefs if not h.startswith("http")]
    for h in local:
        r = await pg.request.get(base + "/" + h)
        check(r.ok, f"Landing page link works: {h}")
    await pg.close()


# ---------------------------------------------------------------- runner
async def main():
    srv, base = serve()
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        await landing(browser, base)
        for w, h, scheme, label in [(1280, 820, "light", "desktop"), (390, 820, "dark", "phone")]:
            for name, fn in [("Spike Lab", spike_lab), ("Relay Lab", relay_lab), ("Prediction Lab", prediction_lab)]:
                print(f"{name} ({label}, {scheme})")
                ctx = await browser.new_context(viewport={"width": w, "height": h}, color_scheme=scheme,
                                                reduced_motion="reduce", has_touch=(w < 500))
                # The labs load their fonts from Google Fonts and fall back to system fonts.
                # Tests must not depend on the network, so font requests get an empty reply.
                await ctx.route(re.compile(r"https://fonts\.(googleapis|gstatic)\.com/.*"),
                                lambda route: route.fulfill(status=200, body="", content_type="text/css"))
                pg = await ctx.new_page(); errors = []
                pg.on("pageerror", lambda e: errors.append(str(e)))
                pg.on("console", lambda m: errors.append(m.text) if m.type == "error" and "fonts" not in m.text else None)
                try:
                    if fn is prediction_lab:
                        await fn(pg, base, behaviour=not (QUICK and w < 500))
                    else:
                        await fn(pg, base)
                except Exception as e:  # report and carry on with the next lab
                    check(False, f"{name}: stopped with {type(e).__name__}: {str(e).splitlines()[0]}")
                width = await pg.evaluate("document.documentElement.scrollWidth")
                check(width <= w, f"{name}: no sideways scrolling at {w}px (page is {width}px)")
                check(not errors, f"{name}: no browser errors {errors[:2]}")
                await ctx.close()
        await browser.close()
    srv.shutdown()
    print(f"\n{'All checks passed.' if not FAILURES else str(len(FAILURES)) + ' check(s) failed.'}")
    sys.exit(1 if FAILURES else 0)


if __name__ == "__main__":
    asyncio.run(main())
