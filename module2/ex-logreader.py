#!/usr/bin/env python

try:
	print "[*] Enter path and target file (e.g. /var/log/syslog)"
	logfile = open(str(raw_input('>')).strip('\n'),'r')
	print "[*] Enter a search string:"
	query = str(raw_input(">")).strip("\n")
except Exception as e:
	print "[-] Error: %r" % e


for i in logfile:
	if i.find(query):
		print "[+] Found log entry: %s" % i

logfile.close()
