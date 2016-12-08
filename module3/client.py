#!/usr/bin/python

from socket import *
import sys

# Create a TCP Client Socket
client = socket(AF_INET, SOCK_STREAM)

# Connect to the target 1<ip> 2<port>
client.connect((sys.argv[1], int(sys.argv[2])))

while 1 :
	userInput = raw_input("Send data to server> ")
	client.send(userInput)				# Send data to server
	print "Server sent:", client.recv(2048)		# Receive and print serve response

# Close connection
client.close()
