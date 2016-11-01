#!/usr/bin/env python

class BadIP(Exception):
	def __init__(self, ip):
		self.ip = ip
		Exception.__init__(self, "Well that didn't go as planned")

	def __str__(self):	# set what's returned as a string if print() or str() is called on this object
		return repr(self.ip) # use repr to print out the string 'representation' of the whatever's in the argument

while True:
	ipaddr = raw_input("Enter valid IPv4 address: ")
	try:
		if len(ipaddr.split('.')) != 4:
			raise BadIP(ipaddr)
	except BadIP as bad:
		print "Sorry, this isn't a valid IP: " + bad.ip
	else:
		print "[+] You gave a valid IPv4 address :)"
