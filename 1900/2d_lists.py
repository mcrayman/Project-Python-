'''
Some examples of 2 dimensional lists
'''

data = [[50 ,20, 23], [20, 6], [14, 8, 3, 0]]

#gives the 3 brackets
print(data[0])
print(data[1])
print(data[2])
print('')

#gives individual values in each bracket
print(data[0][0]) 
print(data[1][0])
print(data[2][3])
print('')

#prints each bracket
for i in data:
	print(i)

print('')

#prints each value in each bracket
for i in data:
	for x in i:
		print(x)

print('')

#add first element of each list (50,20,14)
result = 0
for i in data:
	result += i[0]

print(result)
print('')


for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[i][j])

print('')


def print_odd_elements(data):
	for r in data:
		for i in r:
			if i % 2 != 0:	# COMPLETE THIS LINE
				print(i) # COMPLETE THIS LINE

print_odd_elements(data)
print('')

def count_divisible_elements(data):
	count = 0
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] % 3 == 0:	
				count += 1	
	return count

data = [ [2, 1, 3, 4], [8, 6, 7, 5] ]
result = count_divisible_elements(data)
print(result)

data = [2,10,20,20,45]

print()

for x in data:
	if x >= 12:
	  print(x)
























