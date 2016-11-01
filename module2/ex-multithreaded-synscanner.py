#!/usr/bin/env python
from scapy.all import *
import sys
import threading
import time
#import logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # Disable the annoying No Route found warning
import Queue

# This is going to fetch the tasks
class WorkerThread(threading.Thread):
	''' Constructor takes the queue as input from
	where you're going to fetch your tasks or jobs
	'''
	def __init__(self, queue) :
		threading.Thread.__init__(self) # Calls the parent
		self.queue = queue # assigns queue to internal queue variable
		global tgtHost
		print "[*] Spawning Worker Thread:", self.getName()
	def run(self):
		while True: # Threads always ready to accept new tasks
			port = 0
			# grab port from queue
			try:
				port = self.queue.get(timeout=1) 
				# Note: if timeout not set, thread will block until it gets
			except Queue.Empty: # safely exit if queue empty
				print "[*] Worker Thread Exiting", self.getName()
				return
			# scan the port
			synscan(tgtHost, port, self.queue)
			# signals to queue job is done
			self.queue.task_done()

def synscan(tgtHost, tgtPort, queue):
	response = ""
	response = sr1(IP(dst=tgtHost)/TCP(dport=tgtPort,flags="S"),verbose=0)
	# Check if got any reply at all
	if response.haslayer(TCP):
		# Only checking for SYN ACK == flags == 18
		# filtered ports etc is another story altogether
		if "SA" == response.getlayer(TCP).sprintf("%TCP.flags%"):
		#if response.[TCP].flags == 18 : (ALTERNATIVE)
			print "[+] %d open" % tgtPort

# Create a job queue
portQueue = Queue.Queue(0) # '0' sets number of port jobs to infinite 

# Set values
tgtHost = str(sys.argv[1])
port_min = int(sys.argv[2])
port_max = int(sys.argv[3])
ports = range(port_min, port_max)
num_threads = 10
threads = []

# Loop to spawn n threads and pass it the job queue
for t in range(num_threads):
	# Create a worker thread, passing it the job queue
	worker = WorkerThread(portQueue)
	worker.setDaemon(True) 	# To ensure thread dies when main program dies, ALWAYS USE
	worker.start()
	threads.append(worker) # creating a list of thread names to set a wait command later
# Time the job completions
start = time.time()

# Populate and Define the number of jobs/tasks in queue
for port in ports:
	portQueue.put(port)

# Wait on the queue until everything has been processed 
portQueue.join()

# Wait for all threads to exit
for thread in threads:
	thread.join()

print "[*] Scan completed in:", time.time() - start
