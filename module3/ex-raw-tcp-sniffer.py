#!/usr/bin/env python
import socket
import struct
import binascii

global ETH, IP, TCP, UDP, ICMP, HTTP

ETH, IP, TCP, UDP, ICMP, HTTP = False, False, False, False, False, False
num_packets = 30

def unpackETH(header):
	global IP
	src_mac, dst_mac, eth_type = struct.unpack("!6s6s2s", header)

	print "\n***ETHERNET FRAME HEADER***"
	print "Source MAC:\t\t" + binascii.hexlify(src_mac)
	print "Destination MAC:\t\t" + binascii.hexlify(dst_mac)
	print "Ethernet Type:\t\t" + binascii.hexlify(eth_type)

	if binascii.hexlify(eth_type) == '0800':
		IP = True

def unpackIP(header):
	global TCP, UDP, ICMP
	# Note: the 8x and 2x doesn't get extracted, easy way of disgarding unneeded data
	ttl, proto, src_addr, dst_addr = struct.unpack("!8x B B 2x 4s 4s", header)
	print "\n***IP HEADER***"
	print "Protocol:\t\t" + str(proto)
	print "Source IP:\t\t" + socket.inet_ntoa(src_addr)
	print "Destination IP:\t\t" + socket.inet_ntoa(dst_addr)
	proto = int(proto)

	if proto == 6:
		TCP = True
		print "setting TCP to true"
	elif proto == 17:
		UDP = True
	elif proto == 1:
		ICMP = True

def unpackTCP(header):
	# src_port : 0:2 - H
	# dst_port : 2:4 - H
	# seq_num : 4:8 - L
	# ack_num : 8:12 - L
	# offset : 12:12.5 (nibble)
	# reserved: 12.5-13 (nibble)
	# TCP Flags: 13-14
	# Window: 14-16
	# Checksum: 16-18
	# Urgent Pointer: 18-20
	src_port, dst_port, seq_num,\
			ack_num, offset_reserved_flags, window,\
			checksum, urg_pointer \
			= struct.unpack("! H H L L H H H H", header)

	# Extract Offset, Reserved and Flags fields
	offset = (offset_reserved_flags >> 12) * 4 # See TCP Documentation for why
	flag_urg = (offset_reserved_flags & 32) >> 5
	flag_ack = (offset_reserved_flags & 16) >> 4
	flag_psh = (offset_reserved_flags & 8) >> 3
	flag_rst = (offset_reserved_flags & 4) >> 2
	flag_syn = (offset_reserved_flags & 2) >> 2
	flag_fin = offset_reserved_flags & 1

	# Print Header Info
	print "\n****TCP HEADER****"
	print "Source Port Is:\t\t" + str(src_port)
	print "Dest Port Is:\t\t" + str(dst_port)
	#print "Sequence Number: " + str(seq_num)
	#print "Acknowledgement Number: " + str(ack_num)
	print "Flags:\t\tURG {}, ACK {}, PSH {}, RST {}, SYN {}, FIN {}".format(flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin)
	#print "Offset: " + str(offset)
	#print "Window: " + str(window)
	#print "Checksum: " + str(checksum)
	#print "Urgent Pointer: " + str(urg_pointer)

	if dst_port == 80:
		HTTP = True

def unpackUDP(header):
	src_port, dst_port, length, checksum = struct.unpack("! H H H H", header)

	print "\n****UDP HEADER****"
	print "Source Port:\t\t%d" % src_port
	print "Destination Port:\t\t%d" % dst_port
	print "Length:\t\t%d" % length
	print "Checksum:\t\t%d" % checksum

def unpackICMP(header):
	icmp_type, code, checksum, msg = struct.unpack("! 1s 1s H 4s", header)

	print "\n****ICMP HEADER****"
	print "ICMP Type Code:\t\t%d" % icmp_type
	print "ICMP Code Name:\t\t%s" % str(code)
	print "Checksum: \t\t%d" % checksum

def unpackHTTP(header):
	print data

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
count = 0

while count < num_packets:
	# Sniff a packet
	#pkt = rawSocket.recvfrom(2048)

	#Sniff packets continuously until exit
	pkt, addr = rawSocket.recvfrom(2048)
	print "[+] Got packet on {} interface from remote MAC {}".format(addr[0],\
			binascii.hexlify(addr[4]))

	# Parse Packets
	unpackETH(pkt[0:14])


	if IP:
		unpackIP(pkt[14:34])
		# Note, code may break when capturing packets with ip options enabled,
		# which has a larger header size
	if TCP:
		# the next 20 bytes after IP Header
		unpackTCP(pkt[34:54])
	if UDP:
		pass
	if ICMP:
		pass
	if HTTP:
		unpackHTTP(pkt[54:])

	count += 1
	print "\n[+] Parsed %d packets\n\n" % count
