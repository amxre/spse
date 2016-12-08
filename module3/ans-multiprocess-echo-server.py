#!/usr/bin/python
# Provide the port number via sys.argv[1]

import socket
import thread
import sys
from multiprocessing import Process

def EchoClientHandler(clientSocket, addr):
	while 1:
		client_data = clientSocket.recv(2048)
		if client_data:
			clientSocket.send(client_data)
		else :
			clientsocket.close()
			return

echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

echoServer.bind(("0.0.0.0", int(sys.argv[1]))) # Get port number

echoServer.listen(10) # Set client cue to 10

workerProcesses = []

while 1:
	client, addr = echoServer.accept()
	# Start a new process to service client
	print "Starting new process to service client \n"
	worker = Process(target=EchoClientHandler, args = (client, addr))
	worker.start()
	workerProcesses.append(worker)
