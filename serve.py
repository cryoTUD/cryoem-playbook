"""Simple HTTP server with COOP/COEP headers required by Pyodide/SharedArrayBuffer."""
import http.server, os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = os.path.join(os.path.dirname(__file__), "site")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # suppress per-request logging


if __name__ == "__main__":
    with http.server.HTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Serving site/ at http://127.0.0.1:{PORT}")
        httpd.serve_forever()
