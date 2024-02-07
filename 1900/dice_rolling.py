#simulates rolling 2, 6 sided dice for a large num of trials,
#keeps track of each possible outcome

import random

#how many times to roll dice
n = 100

counts = {}

for i in range(n):
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	outcome = d1 + d2

	if outcome in counts:
		counts[outcome] += 1
	else:
		counts[outcome] = 1




for i in sorted(counts):
	print(f'Count of {i}: {counts[i]}')