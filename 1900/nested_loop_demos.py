
for i in range(30, 33):
	for j in range(40, 35, -1):
		print(f'i = {i}, j = {j}')

'''
runs all values in the range of j for each value in the range of i
i = 30, j = 40
i = 30, j = 39
i = 30, j = 38
i = 30, j = 37
i = 30, j = 36
i = 31, j = 40
i = 31, j = 39
i = 31, j = 38
......
.....etc
'''
print('')

for i in range(10, 17, 2):
	j = 50
	while j > 20:
		print(f'i = {i}, j = {j}')
		j -= 3

#--------------------------------------------
i = 0
while i < 48:
	for j in range(70):
		print(f'That\'s a lot of iterations! {i}')
	i += 1

print(48 * 70)

# ^^^^ prints 3360 iterations, for every value of i < 48, j will be printed 70 times 