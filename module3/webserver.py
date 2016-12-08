#!/usr/bin/python

"""
		Creating a Simple HTTP Server
		Listens on 0.0.0.0 on port 8888
"""
import SocketServer, SimpleHTTPServer

# By default, this serves a directory listing of the dir this script is executed from
class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	# here's an example of customizing the handler when the user
	# requests /admin directory
	# To do this, we overwrite the default do_GET which serves the dirlist
	def do_GET(self):
		if self.path == '/admin':
			# Print out a message to the page
			# PROTIP: Imagine what else you could serve here ;)
			self.wfile.write('\nThis page is only for Admins!\n\n')
			# Additionally also print out the request headers recvd from client
			self.wfile.write(self.headers)
		else:
			# For all other requests, call the default handler
			# which serves the dirlist
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpServer = SocketServer.TCPServer(("", 8888), HttpRequestHandler) # Browse to me
print "[*] Now serving on 0.0.0.0 port 8888, browse to me :)"
httpServer.serve_forever()

