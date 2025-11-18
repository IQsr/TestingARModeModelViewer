# Testing AR Mode Model Viewer

Quick-start recipe to preview `index.html` locally and on iPhone Quick Look.

## Why AR might not work on iPhone
- iOS Quick Look requires the USDZ file to be served with the MIME type `model/vnd.usdz+zip`.
- Safari generally blocks `http` unless you are on `localhost`; testing from another device needs `https` (tunnel or cert).

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

## Files
- `index.html` — `model-viewer` example wired for AR (Quick Look on iOS, Scene Viewer/WebXR on Android/desktop).
- `red_brick_building.glb` — GLB asset for `model-viewer`.
- `Red_Brick_Building.usdz` — USDZ asset for iPhone Quick Look.
- `server.py` — local static server with USDZ MIME type.
