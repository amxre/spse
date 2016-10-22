#!/usr/bin/env python

import os

def child_process () :
	print "I am the child process and my PID is : %d" % os.getpid()

	print "The child is exiting"

def parent_process() :
	print "I am the parent process with PID : %d" % os.getpid()

	# Forking a child to create a new process, it is the exact same replica of the parent
	childpid = os.fork()

	if childpid == 0 :
		# we are in the child process
		child_process()
	else :
		# we are in the parent process
		print "We are inside the parent process"
		print "Our child has the PID : %d"%childpid

	while True :
		pass # while true do nothing

parent_process()
