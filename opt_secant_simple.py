#!/usr/bin/env python3

# Equation optimizer (max and min finder)
import math


# Optimizer
def opt(expr, a, b, tol):
	# expr = expression to find max/min
	# a = start of interval to search for
	# b = end of interval to search for
	# count = how many max/min to look for
	# tol = tolerance/precision of values

	# Tolerance, also value used to approximate derivative
	h = tol*(10**-1)

	# Digits to round to
	digits = -(math.log(tol)/math.log(10))
	digits = int(round(digits, 1))-1

	# Input function
	f = lambda x: eval(expr)

	# Approximate derivative of f(x)
	f_prime = lambda x: (f(x+h)-f(x))/h

	# Find max and min with roots of approximate derivative
	# (using secant/Newton's method)

	n = 0
	while abs(f_prime(n)) > tol:
		# Repeat quasi-Newtons method / Secant method
		n = n - ( f_prime(n) * h/(f_prime(n+h)-f_prime(n)) )
	return (round(n, 2), round(f(n), 2))

def test():
	tests=[
		"x**2-25",
		"x**3-x-2",
		"(x**4)-(8*(x**3))+(2*x)-8"
	]

	for test in tests:
		print("Equation: {}".format(test))
		print("Result: {}\n".format(
			opt(
				expr=test,
				a=-999,
				b=999,
				tol=0.001,
		)
	))

test()
