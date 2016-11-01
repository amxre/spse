#!/usr/bin/python
import optparse, signal, os, sys
from socket import *

def sigalrm_handler(signum, frame):
	print "[*] Time's over, received alarm @ %r seconds" % signum
	sys.exit(0) # Exit gracefully

# Set the Option Arguments
parser = optparse.OptionParser('usage%prog ' +\
		'-s <seconds')
parser.add_option('-s', dest='listen_seconds', type='int',\
		help='specify seconds for server to listen')
# Parse the arguments
options, args = parser.parse_args()
seconds = options.listen_seconds

# Create a tcp server which listen to a port
s = socket(AF_INET, SOCK_STREAM)	# Create a TCP socket
s.bind(('0.0.0.0', 8888))		# Bind to port 8888
s.listen(5)				# Listen but allow
					# no more than 5 pending
					# connections
# Set the SigAlrm Timer
print "[*] Installing signal alarm for %d seconds..." % seconds
signal.signal(signal.SIGALRM,sigalrm_handler)
signal.alarm(seconds)

# Start Accepting Connections
print "[*] Listening on port 8888..."
while True:
	client, addr = s.accept()	# Get a connection
	print "[+] Got a connection %s" % str(addr)

	# Send the client a greeting and close the connection
	client.send("Hello there %s" % str(addr))
	print "[*] Terminating connection to %s" % str(addr)
	client.close()

# Disable the Timer
signal.alarm(0)
