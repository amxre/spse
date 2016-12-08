#!/usr/bin/env python
import socket, struct

# Monitor this with:
# >tcpdump -i eth0 arp
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# Bind Interface for Injection
rawSocket.bind(("eth0", socket.htons(0x0800)))

# Create the Ethernet IP Header (dest_mac, src_mac, eth_type)
packet = struct.pack("!6s6s2s", '\xff\xff\xff\xff\xff\xff', '\xaa\xaa\xaa\xaa\xaa\xaa', '\x08\x06')
# Note:
#	FF:FF:FF:FF:FF:FF = Broadcast Address
#	0806 = ARP Request/Response

# Create ARP Request Payload (28 bytes)
hw_type = '\x00\x01'		# Ethernet (1)
proto_type = '\x08\x00'		# IPv4 (0x0800)
hw_size = '\x06'
proto_size = '\x04'
opcode = '\x00\x01'		# Request (1)
src_mac = '\xaa\xaa\xaa\xaa\xaa\xaa'
src_ip = '\x0a\x02\x00\x02'	# 10.2.0.2
tgt_mac = '\xbb\xbb\xbb\xbb\xbb\xbb'
tgt_ip = '\x0a\x02\x00\x9d'	# 10.2.0.157

payload = struct.pack("! 2s 2s 1s 1s 2s 6s 4s 6s 4s", hw_type, proto_type, hw_size, proto_size, opcode,\
		src_mac, src_ip, tgt_mac, tgt_ip)

# Send Packet
rawSocket.send(packet + payload)
