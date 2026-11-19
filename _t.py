from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/chromium",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1440,"height":900})
    errs=[]
    pg.on("console", lambda m: errs.append(m.type+": "+m.text) if m.type in ("error","warning") else None)
    pg.on("pageerror", lambda e: errs.append("pageerror: "+str(e)))
    pg.goto("http://127.0.0.1:8093/",wait_until="networkidle"); pg.wait_for_timeout(3000)
    pg.screenshot(path="_r/hero.png")
    for name,sel in [("about","#sobre"),("metodo","#metodo"),("trab","#trabalhos"),("visita","#visita")]:
        pg.evaluate(f"window.scrollTo(0, document.querySelector('{sel}').offsetTop-40)")
        pg.wait_for_timeout(1400); pg.screenshot(path=f"_r/{name}.png")
    print("ERROS:", errs[:8])
    m=b.new_page(viewport={"width":390,"height":844})
    m.goto("http://127.0.0.1:8093/",wait_until="networkidle"); m.wait_for_timeout(2500)
    m.screenshot(path="_r/mob.png")
