import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"✅ Server running at http://localhost:{PORT}")
    print(f"📂 Serving files from: {os.getcwd()}")
    print(f"🌐 Open http://localhost:{PORT} in your browser")
    print(f"⏹️  Press Ctrl+C to stop")
    httpd.serve_forever()
