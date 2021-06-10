#!/usr/bin/env python3

# Root finding algorithm with the bisection method
# Finds a single root

import math
def solve(expr, a, b, tol, nmax):
	# Function to find root of
	# Solves x for f(x)=0
	f = lambda x: eval(expr)

	mid = 0
	step = 0

	# Digits to round to, based on tolerance
	digits = -(math.log(tol)/math.log(10))
	digits = int(round(digits, 1))-1

	# Look for answer until max steps reached
	while step <= nmax:
		mid = (a + b)/2
		if f(mid) == 0 or (b - a)/2 < tol:
			# A root has been found
			return round(mid, digits)

		step += 1
		if f(mid) * f(a) >= 0:
			# If the sign of midpoint == sign of LH end
			# set the new LH point to the midpoint.
			# (i.e. search right side of interval)

			a = mid
		else:
			# If the signs of the midpoint and the LH end
			# are not equal, set RH endpoint to the midpoint.
			# (i.e. search left side of interval)
			# (since the LH endpoint and the midpoint have 
			# different signs, a zero (root) must be in between
			# [somewhere in the left side]
			# according to the Intermediate Value Theorem)

			b = mid

tests=[
	"x**2-25",
	"x**3-x-2",
	"2**x-12",
	"4*(x**3)-24*(x**2)+2"
]

for test in tests:
	print("Equation: {}".format(test))
	print("Result: {}\n".format(
		solve(
			expr=test,
			a=-999,
			b=999,
			tol=0.001,
			nmax=999,
		)
	))
