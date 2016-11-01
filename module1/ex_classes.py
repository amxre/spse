#!/usr/bin/env python

# Parent Class
class PortScan(object):	# Parent Class

	def __init__(self, targethost, targetports): # Instance Variables
		print "[*] Parent constructor (__init__) called, args: %s %s" % (targethost, targetports)
		self.host = targethost
		self.ports = targetports

	def sethost(self, targethost):	# Instance Variables
		print '[*] Parent sethost() called, args: %s ' % targethost
		self.host = targethost

	def setports(self, targetports): # Instance variables
		print '[*] Parent setports() called, args: %s ' % targetports
		self.targetports = targetports

	def gethost(self):
		print '[*] Parent gethost() called, return: %s' % self.host

	def getports(self):
		print '[*] Parent getports() called, return: %s' % self.ports

# Child Class
class DefaultPortScan(PortScan):
	defports = [21,22]	# Class Variable

	def __init__(self, targethost):
		print '[*] Child constructor (__init__) called, args: %s' % targethost
		super(DefaultPortScan, self).__init__(targethost, DefaultPortScan.defports)# Intialize Parent w/ default port list
		self.ports = DefaultPortScan.defports # Set default ports via Class Variable

	# Method which will overwrite parent method and return different list of ports
	def getports(self):
		print "[*] Child getports() called, return: %s" % self.ports
		#super(DefaultPortScan, self).getports()

def main():
	# Global Variables
	target = 'google.com'
	ports = [80,443]

	print "[*] Instantiating new PortScan object from Parent class with args: [%s] [%s]" % (target, ports)
	newportscan = PortScan(target, ports) # Instantiating Parent Class object
	newportscan.gethost()
	newportscan.getports()
	newportscan.sethost('youtube.com')
	newportscan.gethost()

	target2 = 'apple.com'

	print "[*] Instantiating new DefaultPortScan object from Child with args: [%s]" % (target2)
	defaultscan = DefaultPortScan(target2)
	defaultscan.gethost() # Inheritance
	defaultscan.getports() # "***My value should be %s***" % defaultscan.defaultports
	defaultscan.sethost('twitter.com')
	defaultscan.gethost()
	defaultscan.setports([110,111])
	defaultscan.getports() # "***My value should be %s***" % defaultscan.defaultports
	print "[*] Child's Default Ports: %s" % defaultscan.defports

if __name__== "__main__":
	main()

