#!/usr/bin/env python3

# Tests of different algorithms for calculating float log2

# O(n) complexity
def log2_a(num):
	ln_2 = 0.693
	# Initial estimate
	log = 32
	# Calculate log2(num) with Newton's method
	for i in range(0, num):
		log = log - (2**log - num) / ((2**log)*ln_2)
	return log


# O(log n) complexity
def log2_b(num):
	ln_2 = 0.693
	# get floor(log2(num))
	log = -1
	x = num
	while (x != 0):
		log += 1
		x = x >> 1
	# refine answer with Newton's method
	for i in range(0, log):
		log = log - (2**log - num) / ((2**log)*ln_2)
	return log


# Faster O(log n) complexity (but less accurate) 
def log2_c(num):
	ln_2 = 0.693
	# find floor(log2(num))
	log = -1
	x = num
	while (x != 0):
		log += 1
		x = x >> 1
	# find closest power of 2 to num
	exp = 1 << log
	if -(exp - num) > ((exp << 1) - num): 
		exp <<= 1
		log += 1
	# Linear approximation with closest power of 2
	log = log + (num - exp) / (exp * ln_2)
	return log

# Builtin function
import math
def log2_d(num):
	log = math.log(num, 2)
	return log


# Tests
import time
import timeit
test_num = 999
iter = 1
print("Test number: {}".format(test_num))
print("Iterations: {}\n".format(iter))

print("N iterations of Newton's method with initial guess of 32:")
print(log2_a(test_num))
tim = timeit.timeit(
  "log2_a({})".format(test_num),
  number = iter
)
print("log2_a time: {0:.6f}\n".format(tim))

print("Bit-shifting + floor(log2(N)) iterations of Newton's method:")
print(log2_b(test_num))
tim = timeit.timeit(
  "log2_b({})".format(test_num),
  number = iter
)
print("log2_b time: {0:.6f}\n".format(tim))

print("Bit-shifting + log2(N) based linear approximation:")
print(log2_c(test_num))
tim = timeit.timeit(
  "log2_c({})".format(test_num),
  number = iter
)
print("log2_c time: {0:.6f}\n".format(tim))

print("math.log():")
print(log2_d(test_num))
tim = timeit.timeit(
  "log2_d({})".format(test_num),
  number = iter
)
print("log2_d time: {0:.6f}\n".format(tim))

