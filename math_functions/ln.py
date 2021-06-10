#!/usr/bin/env python3

import math

# Calculate ln(x) with Taylor series
# ln(x+1) = infinite sum from n=1 of (-1)^(n-1) * (x^n)/n
def ln_a(x):
	# The speed and accuracy of this method depends on
	# it's iterations. More iterations is more accurate
	# but slower.
	iter = (int(x) * 5) + 20
	sum = 0
	sign = 1
	# The domain of the series is (-1,1] so we need to find
	# -ln(1/x) if x>1
	if x > 1:
		x = 1/x
		sign = -1
	# Subtract one because the series finds ln(x+1)
	x -= 1
	for i in range(1, iter):
		s = (-1) ** (i-1)
		sum += s * (x**i / i)
	return sign * sum

# Calculate ln(x) with trapezoidal rule
# ln(x) defined as def. integral 1 to x of (1/t)dt
def ln_b(x):
	n = 1000
	# Changing to 1/x isn't needed to trapezoidal rule, but
	# it improves accuracy
	sign = 1
	if x > 1:
		x = 1/x
		sign = -1
	dx = (x-1)/n
	sum = 1
	for i in range(2, n):
		x_i = 1 + i*dx
		sum += 2*(1/x_i)
	i+=1
	# Last element in sum
	sum += 1/(1 + i*dx)
	sum *= dx/2
	return sign * sum

# Find ln(x) by finding the roots of (e^x)-x
# This speed and accuracy of this method
# depends on the speed and accuracy of the exp() function
# Newton's method
def ln_c(x):
	# Make sure x is a positive integer
	sign = 1
	if x < 1:
		x = 1 / x
		sign = -1
	# Find a good initial guess by finding log2
	# with bit shifts
	log = -1
	n = int(x)
	while (n != 0):
		log += 1
		n = n >> 1
	# Find the root with Newton's method
	iter = 20
	for i in range(0, iter):
		log = log - (math.exp(log)-x)/math.exp(log)
	return sign * log

# Find ln by finding the closest power of 2 (2^a)
# and it's log2 (a). Convert that to ln (multiply by ln(2)),
# then find the ln of x/(2^a) (with Taylor series) and add it # to the ln of the power of 2 (because ln(ab)=ln(a)+ln(b))
# ln(x) = ln(2^a * (x / 2^a)) = ln(2^a) + ln(x/(2^a))
# Logarithm Product Rule
def ln_d(x):
	# Number of iterations for Taylor
	iter = 30
	# if x > 1, just use a Taylor series and return
	if x < 1:
		sum = 0
		x = 1 - x
		for i in range(1, iter):
			sum += (x**i) / i
		return -sum
	# Constant ln(2)
	ln_2 = 0.69314718
	# Find floor(log(2)) of x
	log2 = -1
	n = int(x)
	while (n != 0):
		log2 += 1
		n = n >> 1
	# Convert the log2 into ln
	# ln(2^m) = m * ln(2)
	ln_msb = log2 * ln_2
	# Find 2^floor(log2(x))
	divisor = 1 << log2
	# Find x/(2^a)
	# This value will be in domain [1,2]
	num = x / divisor
	# Find ln(x/(2^a)) with a Taylor series
	sum = 0
	num = 1/num
	num = 1 - num
	for i in range(1, iter):
		sum += (num**i) / i
	# Add the two results of ln together
	return ln_msb + sum

import timeit as tm

def test():
	tests = [5, math.e, 360, 0.5, 500, 1.5]
	funcs = [
		("Taylor series:", "ln_a"),
		("Trapezoid rule:", "ln_b"),
		("Newton's method:", "ln_c"),
		("Logarithm Product Rule:","ln_d")
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
