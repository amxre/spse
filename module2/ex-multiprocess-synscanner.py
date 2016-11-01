#!/usr/bin/env python
from scapy.all import *
import sys
import os
import multiprocessing
def synscan(tgtHost, tgtPorts):
	print "My process Id is %d and I got ports %d to %d" % \
			(os.getpid(), tgtPorts[0],tgtPorts[-1])
	for port in tgtPorts:
		response = ""
		response = sr1(IP(dst=tgtHost)/TCP(dport=port,flags="S"),\
				verbose=0)
		# Check if got any reply at all
		if response.haslayer(TCP):
			# Only checking for SYN ACK == flags == 18
			# filtered ports etc is another story altogether
			if "SA" == response.getlayer(TCP).sprintf("%TCP.flags%"):
			#if response.[TCP].flags == 18 : (ALTERNATIVE)
				print "[+] %d open, PID %d" % (port,os.getpid())

tgtHost = str(sys.argv[1])
#ports = range(sys.argv[2], sys.argv[3])
ports = range(1,1000)

start = time.time()
p1 = multiprocessing.Process(target=synscan, args=(tgtHost,ports[:500],))
p2 = multiprocessing.Process(target=synscan,args=(tgtHost,ports[500:-1],))
p1.start()
p2.start()
p1.join()
p2.join()


print "[*] Scan completed in:", time.time() - start
