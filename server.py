#!/usr/bin/env python3
"""
Simple HTTP server for EU Asylum App
"""

import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

os.chdir('/home/user/asylum-app')

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🚀 EU Asylum Pact App is running!")
    print(f"📱 Open in your browser: http://localhost:{PORT}")
    print(f"")
    print(f"Features:")
    print(f"  ✓ Search by article number, keyword, or theme")
    print(f"  ✓ Browse all 10 legal instruments")
    print(f"  ✓ Access 50+ EUAA practical guidelines")
    print(f"  ✓ Filter by category")
    print(f"  ✓ Direct links to official EUR-Lex documents")
    print(f"")
    print(f"Press Ctrl+C to stop the server")
    print(f"-" * 60)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
