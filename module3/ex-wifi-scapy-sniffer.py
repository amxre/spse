#!/usr/bin/env python
# Create a Wi-Fi Sniffer and print out the unique SSIDs of the
# Wifi networks in your vicinity
from scapy.all import *

print "... Scanning for Beacon frames..."
# Function to parse out SSID names and print them to screen
def get_SSID(packet):
	# Check if it has a Beacon layer
	if packet.haslayer(Dot11Beacon): 
		# Extract the SSID field from the Dot11Elt layer (information layer)
		ssid = str(packet[Dot11Elt].info)
		bssid = str(packet[Dot11].addr3) # BSSID set here for beacons
				# ref: http://www.studioreti.it/slide/802-11-Frame_E_C.pdf
		if not ssid:
			ssid = 'HIDDEN' # for hidden SSID hits
		print "[+] Found SSID:\t" + ssid + ' / ' + bssid 


# Sniff Wifi Beacon Frames to Broadcast
sniff(iface='mon0', prn=get_SSID, store=0 )
