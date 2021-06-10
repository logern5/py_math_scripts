import random as rand

cr_count = 20
gene_count = 2
mut_chance = 0.3
generations = 500

def ga_start():
	pool = [None] * cr_count
	for i in range(cr_count):
		pool[i] = [None] * gene_count
		for j in range(gene_count):
			(pool[i])[j] = rand.randint(97,122)
	return pool

def fitness(cr):
	s1 = 'hi'
	s2 = ''.join(chr(i) for i in cr)
	return 40-sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

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
		"""
		#elem = (pool[idx])[elem_idx]
		bit_pos = rand.randint(1,7) # ASCII is 7 bits
		byt = (1 << bit_pos)
		print(byt)
		(pool[idx])[elem_idx] ^= byt
		"""
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
		print(''.join(chr(i) for i in pool[0]))
		pool_a = crossover(pool[0],pool[1])
		pool = pool_a + pool[:(cr_count-2)]
		pool = mutate(pool)
	pool.sort(key=fitness)
	pool = pool[::-1]
	print("***END***")
	print("Highest fitness score:{}".format(fitness(pool[0])))
	print("Highest fitness chromosome:{}".format(pool[0]))
	str = ''.join(chr(i) for i in pool[0])
	print(str)
gen_alg()
