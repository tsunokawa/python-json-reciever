#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(length).decode('utf-8'))

        print(json.dumps(data, indent=2))

if __name__ == '__main__':
    httpd = HTTPServer(('', 1234), LogHandler)
    httpd.serve_forever()
