# Architecture
The system separates presentation, project persistence, rendering, exports, offline caching, and local serving. Projects persist in IndexedDB under a versioned schema. Rendering uses a background canvas, ordered paint canvases, and a transient effects canvas. All exports are explicitly user initiated.

## Future state
Move compute-intensive fill and image transforms into Web Workers. Introduce a command bus for deterministic history, a portable project bundle, and generated compatibility migrations for previous schema versions.
