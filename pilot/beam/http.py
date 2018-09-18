from threading import Thread
from thread import interrupt_main
from .logging import Log
import click
import os
import json

try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler
except ImportError:
    from http.server import SimpleHTTPRequestHandler

try:
    from SocketServer import TCPServer as HTTPServer
except ImportError:
    from http.server import HTTPServer

    
class http_server(SimpleHTTPRequestHandler):
    def do_GET(self):
        beam_status = json.loads(os.environ['BEAM_STATUS'])
        if self.path == "/":
            self.wfile.write(beam_status['message'])
        self.send_response(beam_status['code'])
        return

    def log_message(self, format, *args):
        return


def run_server(port):
    try:
        httpd = HTTPServer(("", port), http_server)
        httpd.serve_forever()
    except Exception as e:
        click.echo("")
        Log("Error Starting Beam: %s" % (e), fg="red", bold=True)
        interrupt_main()

def start_server(port):
    thread = Thread(target=run_server, args=(port, ))
    thread.daemon = True
    thread.start()
    return 'started http server'
