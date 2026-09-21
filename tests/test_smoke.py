import unittest, subprocess, time, urllib.request, urllib.error, sys
from pathlib import Path
class Smoke(unittest.TestCase):
    def test_server(self):
        root=Path(__file__).resolve().parents[1]
        p=subprocess.Popen([sys.executable,'server.py','--port','5059','--no-browser'],cwd=root,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        try:
            response=None
            for _ in range(20):
                try:
                    response=urllib.request.urlopen('http://127.0.0.1:5059',timeout=1)
                    break
                except urllib.error.URLError:
                    time.sleep(.2)
            self.assertIsNotNone(response,'Local server did not become ready')
            with response as r:
                self.assertEqual(r.status,200)
                self.assertIn(b'Creative Materials Lab',r.read())
        finally:
            p.terminate()
            try:p.wait(timeout=3)
            except subprocess.TimeoutExpired:p.kill()
if __name__=='__main__':unittest.main()
