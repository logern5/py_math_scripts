import random as rand

cr_count = 3
gene_count = 6
mut_chance = 0.2
generations = 40

def ga_start():
	pool = [None] * cr_count
	for i in range(cr_count):
		pool[i] = [None] * gene_count
		for j in range(gene_count):
			(pool[i])[j] = rand.randint(0,5)
	return pool

def fitness(cr):
	return -abs(3-sum(cr))

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

def gen_alg():
	pool = ga_start()
	print("Pool={}".format(pool))
	for gen in range(generations):
		print("Gen={}".format(gen))
		for cr in pool:
			print(fitness(cr))
		pool.sort(key=fitness)
		pool = pool[::-1]
		print("Sorted pool={}".format(pool))
		pool_a = crossover(pool[0],pool[1])
		pool = pool_a + pool[:(cr_count-2)]
		pool = mutate(pool)
		print("Pool={}".format(pool))

gen_alg()
