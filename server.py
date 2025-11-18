import http.server
import mimetypes
import socketserver

# Ensure USDZ files are served with the MIME type required by iOS Quick Look
mimetypes.add_type('model/vnd.usdz+zip', '.usdz')

class Handler(http.server.SimpleHTTPRequestHandler):
    # Serve everything from the current directory
    pass

if __name__ == '__main__':
    port = 8000
    with socketserver.TCPServer(('', port), Handler) as httpd:
        print(f"Serving on http://localhost:{port}")
        print("Note: Use https tunneling (e.g., ngrok/Cloudflare Tunnel) for iPhone testing.")
        httpd.serve_forever()
