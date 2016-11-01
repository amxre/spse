#!/usr/bin/env python
from multiprocessing import Process, Queue
from scapy.all import *
import sys
import Queue as TQ

def WorkerProcess(ip, wid, q):
	
	print "Worker id %d with pid %d created" % (wid,os.getpid())
	while True:
		port = 0
		try:
			# if theres no ports, don't block
			port = q.get(block=False)
		# If Queue empty, handle it gracefully
		except TQ.Empty:
			print "Worker %d with pid %d exiting ..." % (wid,\
					os.getpid())
			return 0 # why?

		# syn scanning to begin, relying on scapy
		response = sr1(IP(dst=ip)/TCP(dport=port,\
				flags="S"), verbose=False, timeout=.2)
		# check for SYN-ACK == flags = 18
		# filtered ports etc. is another story altogether
		if response:
			if response[TCP].flags == 18:
				print "WorkersID %d with pid %d:" % (wid,\
						os.getpid()),
				print "got port %d Status: OPEN""" % (port)
portQueue = TQ.Queue()

for port in range(1,100):
	portQueue.put(port)

worker_ids = []

# Creating worker processes
for wid in range(1,3):
	print "Creating worker with id: %d"% wid
	worker = Process(target=WorkerProcess, args=(sys.argv[1],wid,portQueue))
	worker.start()
	worker_ids.append(worker)

#[IMPROVEMENT] Wait for all processes to finish
for w in worker_ids:
	w.join()

print "All tasks finished"
