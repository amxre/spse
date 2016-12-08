#!/usr/bin/env python

# Create a packet sniffer with Scapy for HTTP
# and print out the HTTP Headers, & GET/POST data

from scapy.all import *

# Ensure Scapy is in Promiscuous Mode
conf.sniff_promisc = True

print "\n[*] Sniffing...\n"

def process_http(packet):

	# check to make sure data has a payload
	if packet[TCP].payload:
		# convert HTTP payload to string for processing
		http_packet = str(packet[TCP].payload)
		if 'GET' in http_packet.upper() or 'POST' in http_packet.upper() or 'HTTP' in http_packet.upper():
			print '\n\n' + ('*' * 60)
			print "[+] Packet Summary:\n" + str(packet.summary()) 
			print "\n[+] HTTP Header:\n" + str(packet[TCP].payload)
			print '*' * 70

# Sniff HTTP Packets
# Runs on all interfaces when 'iface' not specified
# store=0 ensures packets are not kept in memory
#	(so we can keep it running)
if __name__ == "__main__":
	sniff(iface='eth1', filter="tcp port 80", prn =process_http, store=0)

