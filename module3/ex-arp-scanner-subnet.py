#!/usr/bin/env python
# apt-get install python-iface || pip install netifaces
# sudo -H pip install netaddr
# EXERCISE: Expand the code to discover the local subnet automatically

from scapy.all import *
import netifaces # Interface Info https://pypi.python.org/pypi/netifaces/
from netaddr import * # Easy IP / Netmask Calculation http://pythonhosted.org/netaddr/tutorial_01.html#netmasks

print '[*] Available interfaces: ' + str(netifaces.interfaces())
if_name = 'eth1'

# Get Interface Info
if_info = netifaces.ifaddresses(if_name)[netifaces.AF_INET]
if_netmask = if_info[0]['netmask']
if_ip = str(if_info[0]['addr'])
if_mac = netifaces.ifaddresses(if_name)[netifaces.AF_LINK][0]['addr']

# Get Subnet Host List
nw = IPNetwork(if_ip + '/' + if_netmask) # Auto Host/Netmask calculation
host_list = map(str, list(nw)) # Map IP objects to string host ip list
host_list.remove(if_ip)
host_list.remove(str(nw.broadcast))

print "[*] Scanning %s (%s) %s (%d hosts)"% (if_name, if_mac, str(nw.cidr), len(list(nw)))

# Subnet Scanner (ARP Requests)
for ip in host_list:
	arpRequest = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
	arpResponse = srp1(arpRequest, timeout=1, verbose=0)
	if arpResponse :
		print "IP: " + arpResponse.psrc + " MAC: " + arpResponse.hwsrc

