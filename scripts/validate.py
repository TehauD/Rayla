from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=['index.html','static/styles.css','static/js/app.js','static/js/storage.js','server.py','README.md','manifest.webmanifest','service-worker.js']
missing=[x for x in required if not (root/x).is_file()]
for x in required: print(('PASS ' if (root/x).is_file() else 'FAIL ')+x)
text=(root/'index.html').read_text(encoding='utf-8')
for marker in ['/static/styles.css','/static/js/app.js']:
    if marker not in text: missing.append('reference '+marker)
if missing: print('Validation failed:',', '.join(missing));sys.exit(1)
print('Validation passed.')
