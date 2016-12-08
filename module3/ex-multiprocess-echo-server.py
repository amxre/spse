#!/usr/bin/python
# This Server listens on 0.0.0.0:9000
# References: http://docs.python.org/2.7/library/socketserver.html

from SocketServer import TCPServer, ForkingMixIn, BaseRequestHandler
import multiprocessing, os

# Echo Request Handler
class MultiProcessEchoRequestHandler(BaseRequestHandler):
	#allow_reuse_address = True
	#max_children = 10
	def handle(self):
		print "[*] PID (%d) is handling connection from: %s" % \
				(os.getpid(),str(self.client_address))
		data = 'dummy'
		while len(data):	# Run a loop until client sends data, then send it back to client
			data = self.request.recv(1024)
			print "[*] Client sent:", data
			self.request.send(data)
		print "[*] Client left"

class MultiProcessEchoServer(ForkingMixIn, TCPServer): # Multiple Inheritance
	pass

# Port = 0 means to slect an arbitrary unused port
HOST, PORT = "0.0.0.0", 9000

server = MultiProcessEchoServer((HOST,PORT),MultiProcessEchoRequestHandler)	# takes the tuple and your handler class (above)

# Start a Process with the server -- that process will then start one
# more process for each request
server_process = multiprocessing.Process(target=server.serve_forever)
# Exit the server thread when the main thread terminates
server_process.start()
print "[*] Server loop running in process %s (%d)" % (server_process.name, os.getpid())
print "[*] Server Listening on %s %d" % (server.server_address[0], server.server_address[1])
server.serve_forever()
# Cleanup
server.shutdown()
server.server_close()
