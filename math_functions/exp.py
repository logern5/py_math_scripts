#!/usr/bin/env python3

import math

# Calculates e^x where x is a float or int
# Taylor series to calculate e^x
# e^x = infinite sum of (x^n/n!)
def exp_a(x):
	iter = int(x*x) + 10 # Iterations of series grow with x
	sum = 1
	for i in range(iter, 0, -1):
		sum = 1 + (x * sum / i)
	return sum

# Calculate e^x where x is a float or int
# Uses repeated multiplication and a Taylor series
def exp_b(x):
	# Convert into whole and fractional parts
	whole = math.floor(x)
	fract = x - whole
	# Repeatedly multiply the whole part
	result = 1
	for i in range(whole):
		result *= math.e
	if fract == 0.0:
		return result
	# Calculate the fractional part with a Taylor series
	iter = 20
	sum = 1
	for i in range(iter, 0, -1):
		sum = 1 + (fract * sum / i)
	# Multiply the whole and fractional results together
	return result * sum


import timeit as tm
def test():
	tests = [x * 0.5 for x in range(0, 20)]
	funcs = [
		("Taylor series:", "exp_a"),
		("Hybrid of multiplication and Taylor:", "exp_b")
	]
	iter = 10
	for t in tests:
		print("---")
		print("Test: {}".format(t))
		print("Iterations: {}\n".format(iter))
		for f in funcs:
			print(f[0])
			print(eval("{}({})".format(f[1], t)))
			tim = tm.timeit(
				"{}({})".format(f[1], t),
				number = iter
			)
			print("{} time: {:.6f}\n".format(f[1], tim))


test()
