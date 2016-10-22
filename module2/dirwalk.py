#!/usr/bin/env python
import os
 
givenpath = str(raw_input("What is the directory you'd like to walk? "))
	
# traverse a directory, and list directories as dirs and files as files
for cur, dirs, files in os.walk(givenpath):

	_path, path  = cur.split(givenpath) # _ is a throwaway variable, not using it but makes split easier
	# get the path from the base (given) directory to the current walk point
	basepath = path.split('/')
	# use that to calculate how many ... to give
	print (len(basepath) - 1) * '...', os.path.basename(cur)
	for file in files:
		print len(basepath) * '...', file

