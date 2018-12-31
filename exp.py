#!/usr/bin/env python3

def exp(x):
	# Calculates e^x where x is a float or int
	# Taylor series to calculate e^x
	# e^x = infinite sum of (x^n/n!)
	iter = x*x + 10 # Iterations grow with x
	sum = 1
	for i in range(iter, 0, -1):
		sum = 1 + (x * sum) / i
	return sum

def test():
	for i in range(0, 10):
		print("e^{} = {}".format(i, exp(i)))

test()
