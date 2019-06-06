import random

def ga_start():
	cr_count = 6
	gene_count = 4
	pool = [None] * cr_count
	for i in range(cr_count):
		pool[i] = [None] * gene_count
		for j in range(gene_count):
			(pool[i])[j] = random.randint(0,1)
	return pool

print(ga_start())
