#!/usr/bin/env python

class Calculator:

# class contructor, the first function in the object
# first argument in a class is always going to be its self	
	def __init__(self, numa, numb):
		self.a = numa
		self.b = numb

	def add(self):
		return self.a + self.b

	def multiply(self):
		return self.a*self.b

# Creating an instance of the class, outside of the class

newCalculation = Calculator(10, 20)

print 'a+b: %d' % newCalculation.add()

print 'a*b: %d' % newCalculation.multiply()

