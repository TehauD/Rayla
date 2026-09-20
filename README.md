# Rayla's Creative Materials Lab 1.2.0

Engineering-grade, local-first, high-resolution creative workspace. Not a medical device or clinical diagnostic tool.

## Capabilities
- Marker, ink, airbrush, paint, boundary fill, glitter, lava, water, spectrum, motion, and unicorn laser.
- Light, dark, and focus modes.
- Stylus pressure, velocity response, smoothing, opacity, flow, size, and custom color.
- Live FPS, pressure, and stroke telemetry.
- Reproducible JSON session export with settings and event lineage.
- Three 2400 × 1600 canvas layers and lossless PNG export.
- Controlled 220-particle ceiling with cancellation-safe transient effects.
- Local-only custom coloring-page imports.

## Windows
```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\Start-RAYLA.ps1
```

## macOS/Linux
```bash
chmod +x start.sh
./start.sh
```

Open http://127.0.0.1:5050.
