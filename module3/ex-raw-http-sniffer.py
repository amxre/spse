#!/usr/bin/env python
import socket
import struct
import binascii

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

while True:
	# Sniff a packet
	pkt = rawSocket.recvfrom(2048)
	eth_hdr_len = 14 # Assuming ETH's header length will remain constant

	# Unpack IP and get header length
	version_ihl = struct.unpack('!BBHHHBBH4s4s', pkt[0][14:34])
	ip_hdr_len = (version_ihl[0] & 15) * 4

	# Unpack TCP and get header length
	src_port, dst_port, seq_num,\
			ack_num, offset_reserved, flags, window,\
			checksum, urg_pointer \
			= struct.unpack("! H H L L B B H H H", pkt[0][34:54])

	if dst_port == 80:
		print "Source Port Is:\t\t" + str(src_port)
		print "Dest Port Is:\t\t" + str(dst_port)
		tcp_hdr_len = (offset_reserved >> 4) * 4
		print "TCP Header Length: " + str(tcp_hdr_len)
		print 'HTTP Data : ' + pkt[0][eth_hdr_len + ip_hdr_len + tcp_hdr_len:] + '\n\n'
	else:
		del pkt
