# Get user phone number to determine whether toll-free or not

num = int(input('Enter a 10 digit phone number (no spaces or dashes): '))

# get first 3 numbers
area = num // 10000000

code = {800, 888, 877, 866, 855, 844, 833}

#determine if first 3 digits are in 'code'
if area in code:
	print('That number is toll-free!')
else:
	print('That number is not toll-free!')




