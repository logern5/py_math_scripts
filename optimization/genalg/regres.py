# Linear regression using a genetic algorithm
# There are better and easier algorithms for linear regression, this is just an example

import random as rand
import math

cr_count = 10
gene_count = 2
mut_chance = 0.4
generations = 200

# Data to fit equations to
# Expected equation: y=2x+5
data = [(0,5),(2,9),(3,11),(8,21)]

def ga_start():
	pool = [None] * cr_count
	for i in range(cr_count):
		pool[i] = [None] * gene_count
		for j in range(gene_count):
			(pool[i])[j] = rand.randint(0,7)
	return pool

def fitness(cr):
	# Determine how well the model fits using Root Mean Square Error
	m = cr[0]
	b = cr[1]
	n = len(data)
	sum = 0
	for i in data:
		o = i[1]
		f = m * i[0] + b
		sum += (f - o)**2
	rmse = math.sqrt(sum/n)
	return 10-rmse

def crossover(cra, crb):
	p = int(gene_count/2)
	crc = cra[:p] + crb[p:]
	crd = cra[p:] + crb[:p]
	return [crc,crd]

def mutate(pool):
	idx = rand.randint(0,cr_count-1)
	elem_idx = rand.randint(0,gene_count-1)
	if(rand.random() < mut_chance):
		print("Mutation!")
		if(rand.randint(-1,1) > 0):
			(pool[idx])[elem_idx] += 1
		else:
			(pool[idx])[elem_idx] -= 1
	return pool

# Genetic algorithm to fit an equation to data. y=mx+b, gene 0=m, gene 1=b
def gen_alg():
	pool = ga_start()
	print("Pool={}".format(pool))
	for gen in range(generations):
		print("\nGen={}".format(gen))
		pool.sort(key=fitness)
		pool = pool[::-1]
		print("Pool={}".format(pool))
		print("Max fitness={}".format(fitness(pool[0])))
		pool_a = crossover(pool[0],pool[1])
		pool = pool_a + pool[:(cr_count-2)]
		pool = mutate(pool)
	pool.sort(key=fitness)
	pool = pool[::-1]
	print("***END***")
	print("Highest fitness score:{}".format(fitness(pool[0])))
	print("Highest fitness chromosome:{}".format(pool[0]))
	m,b = pool[0]
	print("Approximate equation for data: y={}x+{}".format(m,b))
gen_alg()
