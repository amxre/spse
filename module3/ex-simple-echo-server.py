#!/usr/bin/env python
from socket import *
# Tip: Exit on the client side with CTRL+D (EOF) to get graceful exit of server.
# This simple server handles client sequentially (one at a time)
# and echo's whatever is sent to it back to the client

# Create and start server
s = socket(AF_INET, SOCK_STREAM)	# Create a TCP Socket
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # Allow socket to be reusable incase server
					# is terminated unexpectedly or manually (CTRL-C)
s.bind(('0.0.0.0', 8080))		# Bind to port
s.listen(1)				# No more than 1 concurrent connections
print "[*] Listening on 0.0.0.0:8080"
(client, (ip,port)) = s.accept()	# client = socket, ip = remote client ip
					# port = remote client port

# Alert on connection
print "[+] Got a connection from %s:%s" % (str(ip),str(port))

# Start Echo Output Loop
data = "dummy"
while len(data):			# Echo Loop: Keep receiving data from client until he
					# closes the connection
	data = client.recv(1024)	# When total data reaches this size, exit and close conn
	print "[+] Client sent:", data
	client.send(data)

print "[*] Closing client connection ..."
client.close()

print "[*] Shutting down server ..."
s.close()
