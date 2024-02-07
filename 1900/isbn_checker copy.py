#get user input for a 13-digit isbn

ISBN = int(input('Enter 13-digit ISBN: '))

x1 = int(str(ISBN)[0])
x2 = int(str(ISBN)[1])
x3 = int(str(ISBN)[2])
x4 = int(str(ISBN)[3])
x5 = int(str(ISBN)[4])
x6 = int(str(ISBN)[5])
x7 = int(str(ISBN)[6])
x8 = int(str(ISBN)[7])
x9 = int(str(ISBN)[8])
x10 = int(str(ISBN)[9])
x11 = int(str(ISBN)[10])
x12 = int(str(ISBN)[11])
x13 = int(str(ISBN)[12])

if ISBN > 13:
	print('Error - number exceeds 13 digits')

if (x1 + 3 * x2 + x3 + 3 * x4 + x5 + 3 * x6 + x7 + 3 * x8 + x9 + 3 * x10 + x11 + 3 * x12 + x13) % 10 == 0:
	print('Number is valid!')

else:
	print('Number is invalid!')