import random

def simulate(start_amt, num_rolls):
	purse = start_amt 
	for i in range(num_rolls):
		roll = random.randint(1, 6)
		if roll == 1:
			purse *= 0.5
		elif roll == 6:
			purse *= 1.6
		else:
			purse *= 1.05
	return purse

start = 100
counts = [0] * 5
results = []
total = 0
num_trials = 1000
for i in range(num_trials):
	result = simulate(start, 300)
	total += result
	results.append(result)

	if result < 0.5 * start:
		counts[0] += 1
	elif result <= 0.9 * start:
		counts[1] += 1
	elif result < 1.1 * start:
		counts[2] += 1
	elif result <= 1.5 * start:
		counts[3] += 1
	else:
		counts[4] += 1

avg = total / num_trials

for c in counts:
	print(c)

print(f'Median final purse = ${sorted(results)[num_trials // 2]:.2f}')
print(f'Average final purse = ${avg:.2f}')
