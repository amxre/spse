#!/usr/bin/env python

import sys

#function
def print5times(line_to_print):

	for count in range(0,5) :
		print line_to_print

# Body
print5times(sys.argv[1]) # the command line argument given by the user

