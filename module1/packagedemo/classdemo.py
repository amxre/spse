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
# function to 2 arguments and return the sum
def quickAdd(a,b):
	return a+b
