#!/usr/bin/env python
# This script will handle a SIGINT signal (CTRL C Keyboard Signal: type `man 7 signal` for details
# and mock the user with a message

import signal

def ctrlc_handler(signum, frame):
	print "Haha, you cannot kill me!"

print "Installing signal handler ...."
signal.signal(signal.SIGINT, ctrlc_handler)

print "Done!"

while True: # infinite loop for observing purposes
	pass
