#!/usr/bin/python
# Source: http://ilab.cs.byu.edu/python/select/echoserver.html

import socket
import select
import sys

host = ''	# 0.0.0.0
port = 9000
backlog = 5
size = 1024

# Create a TCP/IP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setblocking(False)
# Bind the socket to the port
print '[*] Starting up on %s port %s' % ('0.0.0.0', port)
server.bind((host, port))
# Listen for incoming connections 
server.listen(backlog)

# This line creates a list of input objects that is initialized to contain
# the server socket and standard input. The server will use this for the
# select() method so that it can wait for both new clients and anything typed
# at the keyboard
input = [server, sys.stdin]

# This starts a while loop, inside the loop the server calls select() to see if
#any of the input sockets (or files) are ready. Note that the server passes two
#additional empty lists to slect,, one for the output sockets and one for the
#exception sockets. In this code, the server doesnt have any sockets of these types.
running = 1
while running:
	# Note that the server uses 3 new lists to capture the return value of the
	# select() call. The server needs to be careful not to overwrite its list
	# of all sockets with the list of sockets ready for input.
	inputready, outputready, exceptready = select.select(input,[],[])

	# The server now starts a for loop to handle any sockets that are
	# 'ready'. Since the server did not specify a timeout for slect,
	# this list should have at least one elemnt in it. Even if it is
	#empty, the server will just loop back to select ?forever?.
	for socket in inputready:
		# 1-Handle the server socket
		if socket == server:
			client, address = server.accept()
			print "[*] Got connection from", address
			input.append(client)

		# Both the server socket and standard input are special cases. For
		# the server socket an input event means a new client is trying to
		# contact the server. The server calls accept() to get the new client
		# and appends the client to its list of input sockets. This means
		# that the net time it calls select() it can handle any input the
		# client has sent on this new socket

		# 2-handle standard input
		elif socket == sys.stdin:
			# Our next special case is input at the keyboard, if this case
			# occurs, the server reads one line from the stdin and then
			#sets the running variable to zero. Thise causes the while loop
			#to terminate after it has handled any pending client requests
			junk = sys.stdin.readline()
			print "[*] Exiting loop, daddy sent:", junk 
			running = 0

		# 3-Handle any client requests
		else:
			# handle all other sockets
			data = socket.recv(size)
			if data:
				print "[*] Client sent:", data
				socket.send(data) # echo back to client
			else:
				print "[*] Client left"
				socket.close()
				input.remove(socket)
			# Finally, the server handles any client requests. It reads data
			# from the socket and if this call succeeds it echoes the data back
			# to the client. If it is unable to read any data, this means the client
			# has closed the connection, so it closes its end of the socket
			# and removes the client from the input list

"""
def EchoClientHandler(clientSocket, addr):
	while 1:
		client_data = clientSocket.recv(2048)
		if client_data:
			clientSocket.send(client_data)
		else :
			clientsocket.close()
			return
"""
