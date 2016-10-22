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

# New sub class which inherits from the parent
class Scientific(Calculator) :
	#This function will calculate the power of a number using pow() function
	def power(self):
		return pow(self.a, self.b)

# Main
# Creating an instance of the class, outside of the class
newCalculation = Calculator(10, 20)

print 'a+b: %d' % newCalculation.add()

print 'a*b: %d' % newCalculation.multiply()

# Creating an instance of the sub class
# notice the inheritance 

newPower = Scientific(2,3)

print 'a+b: %d' % newPower.add() # notice we are using sub to call parent here

print 'a*b: %d' % newPower.multiply()

print 'a pow b: %d' % newPower.power()
