#!/usr/bin/env python3

import math

# Find the power of two floats
# Doesn't work with negative bases

def pow_a(z):
	# Finds the power of x^y where x and y are
	# positive floats or ints.
	# This uses the property a^b = e^(b*ln(a))
	# (exp() of a decimal power can be computed easily
	# [using a Taylor series])

	x = z[0]
	y = z[1]

	# Calculate the exponent
	ln_x = math.log(x)
	return math.exp(y * ln_x)

def pow_b(z):
	x = z[0]
	y = z[1]

	# Find ln(x) using log2 and Taylor Series
	iter = 30
	if x < 1:
		sum = 0
		x = 1 - x
		for i in range(1, iter):
			sum += (x**i) / i
		sum = -sum
		print(sum)
	else:
		ln_2 = 0.69314718
		log2 = -1
		# Find log2 of nearest power of 2 to x, and convert to ln
		n = int(x)
		while (n != 0):
			log2 += 1
			n = n >> 1
		ln_msb = log2 * ln_2
		divisor = 1 << log2
		num = x / divisor
		# Find ln of x/(nearest power of 2)
		sum = 0
		num = 1/num
		num = 1 - num
		for i in range(1, iter):
			sum += (num**i) / i
		# Add results together to get ln(x)
		ln_x = ln_msb + sum

	# Find exp(y * ln(x))
	x = y * ln_x
	neg = False
	if x < 0:
		x = -x
		neg = True
	whole = math.floor(x)
	fract = x - whole
	result = 1
	for i in range(whole):
		result *= math.e
	sum = 1
	if fract != 0.0:
		iter = 20
		for i in range(iter, 0, -1):
			sum = 1 + (fract * sum / i)

	# Return the result
	if neg:
		return 1/(result*sum)
	return result * sum

import timeit as tm
def test():
	tests = [
		(2, 4),
		(7, 0),
		(16, 1.5),
		(9, 0.5),
		(4, -1),
		(2, math.e),
		(13, -2.5),
	]
	funcs = [
		("e^(x ln y) using math lib", "pow_a"),
		("e^(x ln y) without math lib", "pow_b")
	]
	iter = 1
	for t in tests:
		print("---")
		print("Test: {}".format(t))
		print("Iterations: {}\n".format(iter))
		for f in funcs:
			print(f[0])
			print(eval("{}({})".format(f[1], t)))
			tim = tm.timeit(
				"{}({})".format(f[1], t),
				number = iter,
				globals = globals()
			)
			print("{} time: {:.6f}\n".format(f[1], tim))


test()
