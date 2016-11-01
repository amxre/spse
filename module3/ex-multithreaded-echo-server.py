#!/usr/bin/python
# This Server listens on 0.0.0.0:9000
# References: http://docs.python.org/2.7/library/socketserver.html

from SocketServer import TCPServer, ThreadingMixIn, BaseRequestHandler
import threading

# Echo Request Handler with Threading
class ThreadedEchoRequestHandler(BaseRequestHandler):
	#allow_reuse_address = True
	#max_children = 10
	def handle(self):
		print "[*] %s got connection from: %s" % \
				(str(threading.current_thread().name),str(self.client_address))
		data = 'dummy'
		while len(data):	# Run a loop until client sends data, then send it back to client
			data = self.request.recv(1024)
			print "[*] Client sent:", data
			self.request.send(data)
		print "[*] Client left"

class ThreadedEchoServer(ThreadingMixIn, TCPServer): # Multiple Inheritance
	pass

# Port = 0 means to slect an arbitrary unused port
HOST, PORT = "0.0.0.0", 9000

server = ThreadedEchoServer((HOST,PORT),ThreadedEchoRequestHandler)	# takes the tuple and your handler class (above)

# Start a thread with the server -- that thread will then start one
# more thread for each request
server_thread = threading.Thread(target=server.serve_forever)
# Exit the server thread when the main thread terminates
server_thread.daemon = True
server_thread.start()
print "[*] Server loop running in thread:", server_thread.name
print "[*] Server Listening on %s %d" % (server.server_address[0], server.server_address[1])
server.serve_forever()
# Cleanup
server.shutdown()
server.server_close()
