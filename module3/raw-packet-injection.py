#!/usr/bin/env python

import socket, struct

# Monitor this traffic with:
#> tcpdump -i eth0 -vv -XX "not port 22"

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# Specify the interface to do the injection and bind to it
rawSocket.bind(("eth0", socket.htons(0x0800)))

# Create a Simple Ethernet Packet (dest_mac, src_mac, eth_type)
packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')
# Note - 0800 = IPv4 Ethernet Type

rawSocket.send(packet + "Hello there")

