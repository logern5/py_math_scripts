#!/usr/bin/env python3

# Equation solver, using secant method, single root

def solve(expr):
	f = lambda x: eval(expr) # Input function, function to find roots of
	n = 1 # Initial guess
	h = 0.1 # Tolerance
	digits = 1 # Decimal digits to round to
	# Make sure not at max or min
	while f(n+h)-f(n) == 0:
		n += h
	# Find the root
	while abs(f(n)) > h:
		# Repeat Newton's method / Secant method
		n = n - ( f(n) * h/(f(n+h)-f(n)) )
	return round(n, digits)

def test():
	tests=["x**2-25", "x**3-x-2"]
	for test in tests:
		print("Equation: {}".format(test))
		print("Result: {}\n".format(solve(test)))

test()
