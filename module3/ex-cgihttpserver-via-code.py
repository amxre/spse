#!/usr/bin/env python
# Reference: https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
# NOTE: THere's a simpler way to do this with 'python -m CGIHTTPServer 8000

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable() # This line enables CGI Error Reporting

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()

