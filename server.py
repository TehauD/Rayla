from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import argparse, os, webbrowser, threading
class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Referrer-Policy','no-referrer')
        self.send_header('Permissions-Policy','camera=(), microphone=(), geolocation=()')
        super().end_headers()
def main():
    p=argparse.ArgumentParser(description="Run Rayla's Creative Materials Lab")
    p.add_argument('--host',default='127.0.0.1');p.add_argument('--port',type=int,default=5050);p.add_argument('--no-browser',action='store_true');a=p.parse_args()
    os.chdir(Path(__file__).resolve().parent);url=f'http://{a.host}:{a.port}'
    if not a.no_browser: threading.Timer(.8,lambda:webbrowser.open(url)).start()
    print(f'Rayla Lab running at {url}. Press Ctrl+C to stop.')
    try: ThreadingHTTPServer((a.host,a.port),Handler).serve_forever()
    except KeyboardInterrupt: print('\nStopped.')
if __name__=='__main__': main()
