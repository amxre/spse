#!/usr/bin/env python

print "This script will print the numbers between any two given numbers: "

min = int(raw_input("Enter min number: "))
max = int(raw_input("Enter max number: "))

while min <= max:
	if max - min > 25:
		print "Please keep the gap <25, dont wanna flood your screen =/"
		break
	min += 1
	print min
else:
	print "Fin!"
