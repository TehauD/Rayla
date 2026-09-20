from pathlib import Path
J=Path("static/app.js").read_text();H=Path("static/index.html").read_text();C=Path("static/styles.css").read_text()
def test_materials():
 for x in ["glitter","lava","water","spectrum","motion","air","bucket"]: assert x in J
def test_controls():
 for x in ["pressureOn","velocityOn","telemetry","session"]: assert x in H
def test_safety(): assert "const LIMIT=220" in J
def test_theme(): assert "data-theme" in H and "data-theme=dark" in C
