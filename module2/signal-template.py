#!/usr/bin/env python
# Use this code to create a template for anything using a signal

import signal, sys

def SigAlarmHandler(signal, frame):
	print "Receiving alarm ... shutting down..."
	sys.exit(0)

signal.signal(signal.SIGALRM, SigAlarmHandler)
signal.alarm(100) # 100 seconds

print "Starting work.. waiting for alarm to quit.."
# Your work here
while True:
	# do something
	pass

signal.alarm(0) # Disable alarm
