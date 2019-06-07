#!/usr/bin/python3

# Find nth root of x with Newton's method
def nth_root(n, x):
	root = x / n*n
	tol = 0.1
	# Iterate until within tolerance
	while abs(x - root**n) > tol:
		root = root - (root**n - x) / (n * root**(n-1))
	return root

# Tests
import timeit as tm
def test():
	tests = [
		(5, 1024),
		(3, 125)
	]
	funcs = [
		("Newtons method","nth_root")
	]
	iter = 1
	for t in tests:
		print("---")
		print("Test: {}".format(t))
		print("Iterations: {}\n".format(iter))
		for f in funcs:
			print(f[0])
			print(eval("{}({},{})".format(f[1], t[0], t[1])))
			tim = tm.timeit(
				"{}({},{})".format(f[1], t[0], t[1]),
				number = iter,
				globals = globals()
			)
			print("{} time: {:.6f}\n".format(f[1], tim))


test()
