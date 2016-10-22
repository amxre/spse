#!/usr/bin/env python

f = open("/var/log/auth.log", "r")

for line in f.readlines():
	if line.find("root") != -1:
		print line

f.close() 
