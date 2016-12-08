#!/usr/bin/python
# Reference: http://ilab.cs.byu.edu/python/select/echoserver.html
# Non-blocking Multiplexed TCP Server

import socket, select, sys

host = ''	# 0.0.0.0
port = 9000
backlog = 5
size = 1024

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print '[*] Starting up on %s port %s' % ('0.0.0.0', port)
tcpSocket.bind((host, port))
tcpSocket.listen(backlog)

# This line creates a list of input objects that is initialized to contain
# the server socket and standard input. The server will use this for the
# select() method so that it can wait for both new clients and anything typed
# at the keyboard
socketList = [tcpSocket, sys.stdin]

running = 1 # 1 == True
while running:
	inputready, outputready, exceptready = select.select(socketList,[],[])

	for s in inputready:
		# 1-Handle the server socket
		if s is tcpSocket: # same as 'if socket == server'
			clientSocket, address = tcpSocket.accept()
			print "[*] Got connection from", address
			socketList.append(client)

		# 2-handle standard input
		elif s is sys.stdin:
			junk = sys.stdin.readline()
			print "[*] Exiting loop, daddy sent:", junk
			running = 0

		# 3-Handle any client requests
		else:
			# handle all other sockets
			data = s.recv(size)
			if data:	# If client sent data
				print "[*] %s sent: %s" % (address, data)
				# echo back to client
				clientSocket.send("[+] Client you sent the server this:" + data)
				# Food for thought: How does s.send() and clientSocket.send() do the same thing?
			else:		# Assuming client left and closing the connection
				print "[*] %s left, closing the connection" % (address)
				s.close() # Food for thought: How does do the same thing as clientSocket.close()?
				socketList.remove(s)
