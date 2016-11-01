#!/usr/bin/env python

import os
import sys

print "[*] Input directory to list:"
targetdir = sys.argv[1]


for (dirpath, dirname, filelist) in os.walk(targetdir):
	for d in dirname:
		startpath = dirpath.split(targetdir)[1] #get the path, not the blank space at [0]
		depth_from_target_path = len(startpath.split('/')) - 1
		print ("----" * depth_from_target_path) + "[%s]" % d
		for f in filelist:
			print ("----" * (depth_from_target_path + 1)) + f

print "[+] Finished"
