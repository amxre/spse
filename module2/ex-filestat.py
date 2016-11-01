#!/usr/bin/env python

import os
# Various functions to manipulate time values, especially for os.stat()
import time # ST_MTIME 
import sys
#This module provides access to the unix password database, for converting ST_UID to username
import pwd # ST_UID, ST_GID 
# Constants/functions for interpreting results of os.stat()/os.lstat()
from stat import * # ST_SIZE

filename = sys.argv[1]

try:
	# os.stat() returns a tuple with the following ST_MODE, ST_INO, ST_DEV, ST_NLINK, ST_UID, ST_GID, ST_SIZE, ST_ATIME, ST_MTIME, ST_CTIME
	st = os.stat(filename)
	print "[*] Processing file", filename
except IOERROR:
	print "[-] Failed to get information about", filename
else:
	print "[+] File Location:", os.path.abspath(filename)
	print "[+] File size:", st.st_size, "bytes"
	#print "[+] Creation time:", st_size  << Impossible to get in Linux
	# time.asctime([tuple]) converts a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'
	# time.localtime([seconds]) converts seconds since Epoc to a time tuple expressing local time
	print "[+] File modified (mtime):", time.asctime(time.localtime(st[ST_MTIME]))
	print "[+] Last accessed (atime):", time.asctime(time.localtime(st[ST_ATIME]))
	print "[=} Last ownership/permission change (ctime)", time.asctime(time.localtime(st[ST_CTIME]))
	print "[+] File owner:", pwd.getpwuid(st.st_uid).pw_name, # Convert UID to username
	print "UID:", st.st_uid
	print "[+] Group ID of owner:", st.st_gid
	#print "[+] Device:", st.st_dev
