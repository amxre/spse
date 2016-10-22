#!/usr/bin/python

class Calculator:

	def __init__(self, ina, inb):
		self.a = ina
		self.b = inb

	def add(self):
		return self.a + self.b

	def multiply(self):

		return self.a * self.b

class Scientific(Calculator) :

	def power(self):
		return pow(self.a, self.b)



def quickAdd(a,b):
	return a+b


