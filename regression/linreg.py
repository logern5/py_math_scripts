import math
def reg(data):
	# http://www.stat.ucla.edu/~rosario/classes/091/112-1b/regression.pdf
	# get x and y components from data
	x, y = zip(*data)
	n = len(data)
	x_mean = sum(i for i,j in data)/n
	print(x_mean)
	y_mean = sum(j for i,j in data)/n
	print(y_mean)
	s_x = math.sqrt(
		sum((i - x_mean)**2 for i,j in data)/(n-1)
	)
	print(s_x)
	s_y = math.sqrt(
		sum((j - y_mean)**2 for i,j in data)/(n-1)
	)
	print(s_y)
	r = sum((i - x_mean) * (j - y_mean) for i,j in data)/((n-1) * s_x * s_y)
	print(r)
	# y = mx+b, or y = bx+a, etc
	m = r * (s_y/s_x)
	print(m)
	b = y_mean - m*x_mean
	print(b)
dat = [(10,40), (20,40), (40,60), (45,80), (60,90), (65,110)]
reg(dat)
