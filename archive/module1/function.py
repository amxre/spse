#!/usr/bin/env python
import sys


def print5times(line_to_print):

	for count in range(0,5) : 
		print line_to_print

# command line argument given by user
print5times(sys.argv[1])
