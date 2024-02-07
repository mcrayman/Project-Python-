# loop examples
'''
stuff = 'sloths are nice'

i = 0
while i < len(stuff):
	print(stuff[i])
	i += 1

for i in stuff:
	print(i)

for i in range(4): #range(4) = 0,1,2,3
	print(i)

for i in range(4, 8): #range(4,8) = 4,5,6,7
	print(i)

for i in range(4,8,2): #range(4,8,2) = 4,6	the '2' is the amount to skip, excluding final number
	print(i)


for i in range(18,86,4):
	print(i)

i = 105
while i > 0:
	print(i)
	i -= 5

	'''
for x in range(105, 0, -5):
	print(x)
