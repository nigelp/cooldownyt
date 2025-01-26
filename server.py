from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from download import download_youtube_content
from urllib.parse import urlparse
from urllib.parse import parse_qs
import os
import subprocess
import platform

class DownloadHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response = "Cooldown YT Server is running"
        self.wfile.write(response.encode())
 
    def do_GET(self):
        if self.path == '/open-downloads':
            downloads_path = os.path.join(os.getcwd(), 'downloads')
            try:
                if platform.system() == "Windows":
                    os.startfile(downloads_path)
                elif platform.system() == "Darwin":
                    subprocess.run(["open", downloads_path])
                else:
                    subprocess.run(["xdg-open", downloads_path])
                
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = "Cooldown YT Server is running"
            self.wfile.write(response.encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        if self.path == '/download':
            try:
                data = json.loads(post_data.decode('utf-8'))
                url = data.get('url', '')
                audio_only = data.get('audioOnly', False)
                
                if not url:
                    raise ValueError('URL is required')
                
                parsed_url = urlparse(url)
                if 'youtube.com' not in parsed_url.netloc and 'youtu.be' not in parsed_url.netloc:
                    raise ValueError('Invalid YouTube URL')
                
                download_youtube_content(url, audio_only=audio_only)
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())

def run(server_class=HTTPServer, handler_class=DownloadHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()