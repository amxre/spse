# Scapy Injection and Forging
#Create a packet
pkt = IP(dst=‘google.com’)
pkt= IP(dst=‘google.com’)/ICMP()/‘Ben was here’

# Layer 3 : Send Packet
send(pkt)
sudo tcpdump -i eth1 -XX -vvv icmp

# Layer 2 : Send and create packet at same time at Layer 2
# Note - you need to specify the interface when using sendp()
#	Sends 1 Packet
sendp(Ether()/IP(dst='google.com')/ICMP()/"XXX", iface='eth1')
# 	Sends Packets continuously in loop
sendp(Ether()/IP(dst=‘google.com’)/ICMP()/“XXX”, iface=‘eth1’, loop=1)
#	Sends Packet continuously in loop with 1 second interval
sendp(Ether()/IP(dst='google.com')/ICMP()/"XXX", iface='eth1', loop=1, inter=1)


#Send and Receive
# Layer 2 - Note: you need to specify Ether() layer
srp() # returns answers and unanswered packets
srp1() # returns only answer or sent packets
srp1(Ether()/IP(dst=‘google.com’, ttl=22)/ICMP()/‘XXX’)
# Layer 3
sr() # same as above
sr(IP(dst='google.com')/ICMP()/'XXX')
sr1() # same as above
sr1(IP(dst=‘google.com’), timeout=3)

# routing
conf.route.add(host=‘192.168.1.10’, gw=‘192.168.1.22’)
conf.route.resync()
