# Genetic algorithm to find a solution for 4 numbers that add up to 3

import random as rand

cr_count = 6
gene_count = 4
mut_chance = 0.2
generations = 20

# Create initial gene pool
def ga_start():
	pool = [None] * cr_count
	for i in range(cr_count):
		pool[i] = [None] * gene_count
		for j in range(gene_count):
			(pool[i])[j] = rand.randint(0,5)
	return pool

def fitness(cr):
	# The most fit solution has a sum closest to 3
	# Highest score is 10
	return -abs(3-sum(cr))+10

# Cross over chromosomes cra and crb into two new offspring
def crossover(cra, crb):
	p = int(gene_count/2)
	crc = cra[:p] + crb[p:]
	crd = cra[p:] + crb[:p]
	return [crc,crd]

# Mutate a random gene on a random chromosome given by probability mut_chance
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

# Genetic algorithm to find an optimal solution to the problem of finding numbers that sum to 3
def gen_alg():
	# Get initial gene pool
	pool = ga_start()
	print("Pool={}".format(pool))
	# Run genetic algorithm for specified
	for gen in range(generations):
		print("\nGen={}".format(gen))
		# Sort gene pool by fittest chromosome (given by fitness function)
		pool.sort(key=fitness)
		pool = pool[::-1]
		print("Pool={}".format(pool))
		print("Max fitness={}".format(fitness(pool[0])))
		# Crossover the two fittest parents and create two new offspring
		pool_a = crossover(pool[0],pool[1])
		# Create a new gene pool with the new offspring and the fittest of the last generation
		pool = pool_a + pool[:(cr_count-2)]
		# Randomly mutate a random gene on a random chromosome
		pool = mutate(pool)
	pool.sort(key=fitness)
	pool = pool[::-1]
	print("***END***")
	print("Highest fitness score:{}".format(fitness(pool[0])))
	print("Highest fitness chromosome:{}".format(pool[0]))
gen_alg()
