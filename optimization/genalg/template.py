import random as rand

cr_count = 5
gene_count = 4
mut_chance = 0.2
generations = 20

def ga_start():
	pool = [None] * cr_count
	for i in range(cr_count):
		pool[i] = [None] * gene_count
		for j in range(gene_count):
			(pool[i])[j] = rand.randint(0,5)
	return pool

def fitness(cr):
	return -abs(3-sum(cr))+20

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
gen_alg()
