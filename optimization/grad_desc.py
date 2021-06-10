import numpy as np

def obj_func(params):
	x = params[0]
	y = params[1]
	# Minima are (-1, 12)
	return (x + 1)**2 + (y - 12)**2

def calc_gradient(f, params):
	# h value for finite differnce approximation of derivative
	h = 0.0001
	# Calculate the gradient by calculating partial derivatives w.r.t each variable
	partials = np.empty(len(params))
	# Calculate partial derivatives with central finite difference approximation: (f(x + h) - f(x - h)) / 2h
	for i in range(len(params)):
		upper_params = params.copy()
		upper_params[i] += h
		lower_params = params.copy()
		lower_params[i] -= h
		partials[i] = partial_i = (f(upper_params) - f(lower_params)) / (2 * h)
	return partials

def calc_step_size(f, grad, position, gamma):
	# f = function, v = negative gradient, a = current position
	c = 0.5
	v = np.multiply(grad, -1)
	ready = False
	while not ready:
		left_side = f(position + (gamma * v))
		norm_sq = np.linalg.norm(grad) ** 2
		right_side = f(position) - (c * gamma * norm_sq)
		if(left_side > right_side):
			gamma /= 2
		else:
			ready = True
	return gamma

def grad_desc(f, params):
	position = np.array(params).astype(float)
	step_size = 50
	done = False
	tresh = 0.00000001
	# Loop until the magnitude (norm) of the gradient is close to zero
	while not done:
		current_gradient = calc_gradient(f, position)
		if(np.linalg.norm(current_gradient) < tresh):
			done = True
			break
		# Find optimum step size
		step_size = calc_step_size(f, current_gradient.copy(), position.copy(), step_size)
		# Descend in the direction and magnitude of the gradient times the step size
		position = position - (step_size * current_gradient)
	return position

# We should get (-1, 12) for the minimum of the function
position = grad_desc(obj_func, [7,3])
print(position)
