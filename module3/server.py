#!/usr/bin/python

# This is an "echo" server
# accepts a string from a client and echo it back

import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ensure the address and port is reusable if server crashes unexpectedly
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))

tcpSocket.listen(2)


print "Waiting for a Client..."
(client, ( ip, sock)) = tcpSocket.accept()

print "Receiving connection from : ", ip

print "Starting ECHO output .... "

data = 'dummy'

while len(data) :
	data = client.recv(2048)
	print "Client sent: ", data
	client.send(data)


print "Closing connection ..."
client.close()

print "Shutting down server ..."
tcpSocket.close()
