#!/usr/bin/env python
from ftplib import FTP
import threading
import Queue
import sys
import time

# List of anonymous login FTP sites
hosts = [	"10.2.0.129",
		"ftp.x.org",
		"ftp4.FreeBSD.org",
		"ftp.ncsa.uiuc.org",
		"ftp.mozilla.org",
		"ftp.crans.org"
	]

class WorkerThread(threading.Thread):
	def __init__(self, q, tid):
		threading.Thread.__init__(self)
		self.q = q
		self.tid = tid # Thread ID
		self.lock = threading.Lock()
		print "[*] Spawning worker thread: %d" % self.tid

	def run(self):
		while True:
			host = None
			# grab host from queue
			try:
				host = self.q.get(timeout = 1)
			except Queue.Empty:
				print "[*] Worker Thread %d exiting" % self.tid
				return	# Why is there a return?

			#Acquire Print Lock while printing output
			self.lock.acquire()
			print "Thread %d acquired lock" % self.tid

			# Main Job Here
			try:
				# connect to ftp host on default port
				ftp = FTP(host, timeout=2) 
				# login with user anonymous, password ""
				ftp.login()
				print "[+] Thread %d Successful login to %s" % (self.tid,host)
				# change directory to "/"
				#ftp.cwd("/")
				# get directory listing and print
				print ftp.retrlines('LIST')
				ftp.quit()
			except :
				print "[-] Thread %d Got error wit host: %s" % (self.tid,host)
			finally:
				#Release the Lock
				print "[-] Thread %d releasing lock" % self.tid
				self.lock.release()
				#raise

			# Signal task is done
			self.q.task_done()

# Set Values
hostQueue = Queue.Queue()
threads = []

# Spawn the 5 threads
for t in range(5):
	worker = WorkerThread(hostQueue, t)
	worker.setDaemon(True)
	worker.start()
	threads.append(worker)

# Populate the queue
for host in hosts:
	hostQueue.put(host)

# Wait for jobs to finish
hostQueue.join()

# Wait for threads to finish
for thread in threads:
	thread.join()

print "[*] Fin!"
