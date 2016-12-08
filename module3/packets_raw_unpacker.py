#!/usr/bin/env python

import socket
import struct
import binascii

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# Sniff a packet
pkt = rawSocket.recvfrom(2048)

print "####ETHERNET HEADER####"
# Extract Ethernet Header from packet - first 14 bytes
ethernetHeader = pkt[0][0:14]
# Unpack Source Mac, Dest Mac, and Eth Type in Network Byte Order (!)
eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)

print "Source Mac: " + binascii.hexlify(eth_hdr[0])

print "Destination Mac: " + binascii.hexlify(eth_hdr[1])

print "Ethernet Type: " + binascii.hexlify(eth_hdr[2])

print "#####IP HEADER#####"
# Extract IP Header from packet - The next 20 bytes in the packet
ipHeader = pkt[0][14:34]

# Unpack the Source and Destination IP Address
ip_hdr = struct.unpack("!12s4s4s", ipHeader)

# Print the Source and Destination IP
print "Source IP Address: " + socket.inet_ntoa(ip_hdr[1])
print "Destination IP Address: " + socket.inet_ntoa(ip_hdr[2])


print "#####TCP HEADER######"
# Extract TCP Header from packet - the next 20 bytes after IP Header
tcpHeader = pkt[0][34:54]
# Unpack TCP Header
tcp_hdr = struct.unpack("!HH16s", tcpHeader) # Format: Source Port, Dest Port, rest of packet

# Print Source and Destination Port
print "Source Port Is: " + str(tcp_hdr[0])
print "Dest Port Is: " + str(tcp_hdr[1])

