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



newCalculation = Calculator(10, 20)

print 'a+b: %d' % newCalculation.add()

print 'a*b: %d' % newCalculation.multiply()

newPower = Scientific(2, 3)

print 'a+b: %d' % newPower.add()

print 'a*b: %d' % newPower.multiply()

print 'a pow b: %d' % newPower.power()




