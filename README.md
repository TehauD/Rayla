# Rayla's Creative Materials Lab 2.0.0

A local-first, high-resolution creative studio for imaginative drawing, coloring, material experimentation, and durable artwork management.

**No ads. No accounts. No tracking. Just creativity.**

## What is included

- Marker, ink, airbrush, paint, fill, glitter, lava, water, spectrum, motion, unicorn laser, and eraser tools
- 2400 × 1600 layered canvas
- Stylus pressure, velocity sizing, smoothing, opacity, flow, and custom colors
- Built-in coloring pages, local image import, stickers, and bounded effects
- Undo, redo, clear confirmation, zoom, fit, focus, light, dark, and reduced-motion modes
- Editable multi-layer projects
- Automatic local recovery and an IndexedDB artwork gallery
- PNG artwork export and JSON session export
- Progressive Web App shell and offline asset cache
- Structured repository validation and smoke testing

## Start on Windows

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\Start-RAYLA.ps1
```

## Start on macOS or Linux

```bash
chmod +x start.sh
./start.sh
```

Open `http://127.0.0.1:5050`. Python 3.11 or later is recommended.

## First workflow

1. Select a coloring page or Free Draw.
2. Select a material and color.
3. Create artwork with mouse, touch, or stylus.
4. Add layers for nondestructive experimentation.
5. Choose **Save Project** to persist the editable project locally.
6. Open **Gallery** to resume, review, or delete saved artwork.
7. Export a flattened PNG or session JSON when needed.

## Privacy

The application runs locally and does not implement accounts, analytics, advertising, cloud upload, camera access, microphone access, or location access. Projects are stored in the browser's IndexedDB database. Clearing site data can remove saved projects, so export important artwork.

## Architecture

```text
Browser UI
├── Canvas engine
│   ├── Background canvas
│   ├── Editable paint layers
│   └── Transient effects canvas
├── IndexedDB project storage
├── PNG and JSON export
├── Service worker cache
└── Local Python HTTP server
```

## Project format

Saved projects use `rayla.project.v2` and contain metadata, background content, editable layer data, settings, metrics, event lineage, and a gallery thumbnail. The schema is versioned to support future migration.

## Validation

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

## Current constraints

- Flood fill operates on the active layer and can be expensive on large regions.
- Undo uses full-resolution snapshots and is capped at 20 states.
- Browser-local projects are tied to the local origin and browser profile.
- PWA install behavior differs by browser and operating system.
- Project data is local, not synchronized between devices.

## Recommended next engineering increments

- Move flood fill into a Web Worker with cancellation and progress.
- Add layer rename, reorder, visibility, lock, and opacity controls directly in the layer panel.
- Add selection, transform, crop, rotate, and canvas navigation gestures.
- Replace full-canvas undo snapshots with tile-based or command-based history.
- Add Playwright and Axe end-to-end coverage.
- Add project import/export as a portable `.rayla` bundle.
- Add child and advanced workspace modes through progressive disclosure.

## Safety and scope

This is a creative application. It is not a medical device, diagnostic tool, educational assessment system, or safety-monitoring platform. A parent or guardian should review imported files and files shared outside the application.

## Repository files

```text
index.html
static/styles.css
static/js/app.js
static/js/storage.js
server.py
Start-RAYLA.ps1
start.sh
manifest.webmanifest
service-worker.js
scripts/validate.py
tests/test_smoke.py
.github/workflows/validate.yml
```

## License

No reuse license is granted until the repository owner adds a `LICENSE` file.
