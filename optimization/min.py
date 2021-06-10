
import math

# Cost is sum of squares of residuals
def cost(func, data, params):
    n = len(data)
    #print("Called with params:{}".format(params))
    sum = 0
    for elem in data:
        k = (elem[1] - func(elem[0],params))**2
        #print("k: {}".format(k))
        sum += k
    #print("Sum:{}".format(sum))
    return sum
    
def opt(func, data, params):
    #print("opt()")
    l = len(params) # number of parameters for the function
    grad = [0]*l # gradient
    old_grad = list(grad) # previous gradient, used for calculating gamma
    vec = params # vector of solution parameters
    cst = 1 # cost
    gamma = 0.01 # initial gamma (change) value
    h = 0.01 # constant for numerical differentiation to calculate gradient
    max_iter = 500 # number of iterations to stop after
    j = 0 # counter
    gn = 1 # numerator of gamma function
    cost_threshold = 0.02 # maximum acceptable cost
    # calculate standard deviation for cost analysis
    stdev = 0
    ssum = 0
    n = len(data)
    mean = sum(i[1] for i in data)/n
    #print(mean)
    for d in data:
        ssum += (d[1] - mean)**2
    ssum /= n
    #print(ssum)
    ss_tot = ssum
    stdev = math.sqrt(ssum)
    grad_norm = 2
    while (cst > cost_threshold) and (j < max_iter):
        old_grad = list(grad)
        # calculate gradient
        for i in range(l):
            vec2 = list(vec)
            vec2[i] += h
            grad[i] = (cost(func, data, vec2)-cost(func, data, vec))/h
        # Calculate sum of gradients for gamma value
        ssum = 0
        #print("Grad:{}".format(grad))
        for i in range(l):
            k = grad[i] - old_grad[i]
            ssum += k
            #print("K:{}".format(k))
        # Calculate gamma value
        # Gamma is inversely proportial to the magnitude of the difference between the new and old gradients
        ssum = abs(ssum)
        if ssum == 0:
            break
        gamma = gn/ssum
        #print(ssum)
        if(gamma > 10):
            gamma = 10
        # adjust solution vector
        for i in range(l):
            vec[i] -= gamma * grad[i]
        cst = cost(func, data, vec)/ss_tot
        print("Current cost:{}".format(cst))
        j += 1
        for elem in grad:
            grad_norm += elem**2
        grad_norm = math.sqrt(grad_norm)
        print("step size:{}".format(gamma))
    print("cst:{}".format(cst))
    return vec
        
def f(x, params):
    return params[0]*(x**2) + params[1]*x + params[2]
d = [(2,8),(3,12),(4,16),(5,22)]

vec = opt(f, d, [1,1,1])
print("Data:{}".format(d))
print("Vec:{}".format(vec))
print("Cost: {}".format(cost(f, d, vec)))

def f2(x, params):
    return params[0] * (x**2)
d2 = [(0.43,0.5),(0.54,1),(0.71,1.5),(0.76,2)]
#Desmos: a = 3.24..

vec = opt(f2,d2,[1])
print("Data:{}".format(d2))
print("Vec:{}".format(vec))
print("Cost: {}".format(cost(f2, d2, vec)))
