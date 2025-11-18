# Testing AR Mode Model Viewer

Quick-start recipe to preview `index.html` locally and on iPhone Quick Look.

## Why AR might not work on iPhone
- iOS Quick Look requires the USDZ file to be served with the MIME type `model/vnd.usdz+zip`.
- Safari generally blocks `http` unless you are on `localhost`; testing from another device needs `https` (tunnel or cert).
- GitHub Pages can return `404` if assets are not in the expected path; the page now surfaces a warning banner when the USDZ/GLB
  cannot be fetched.

## Run a local server with correct MIME type
```bash
python3 server.py
```
- Serves files from this folder at `http://localhost:8000`.
- The server registers the required USDZ MIME type for Quick Look.

## Test on a physical iPhone
1. If using the same machine: open Safari and visit `http://localhost:8000`.
2. If using another device: expose the server via a tunnel (e.g., `ngrok http 8000`) to get an `https` URL.
3. Tap the "View in your space" button; Quick Look should launch the `.usdz` asset.

## GitHub Pages notes (AR button missing?)
- GitHub Pages serves over **HTTPS**, which is required for iOS AR.
- The page now shows an iOS Quick Look link **by default**, hiding it only on non-iOS devices via JS. This keeps the AR entry point visible even if GitHub Pages caching prevents `model-viewer` from rendering the AR button or if client-side JS fails to execute.
- If you see a yellow banner at the top, it means the `.usdz` or `.glb` could not be fetched (likely a wrong path or 404 on GitHub Pages). Fix the path or upload the asset and refresh.
- If you host elsewhere and control headers, set `Content-Type: model/vnd.usdz+zip` for `.usdz` so Quick Look opens reliably.

## Files
- `index.html` — `model-viewer` example wired for AR (Quick Look on iOS, Scene Viewer/WebXR on Android/desktop).
- `red_brick_building.glb` — GLB asset for `model-viewer`.
- `Red_Brick_Building.usdz` — USDZ asset for iPhone Quick Look.
- `server.py` — local static server with USDZ MIME type.
