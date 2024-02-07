# this program determines if a user-input integer is prime. 

n = int(input('Enter an integer:'))

if n < 2:
	print(f'{n} is not prime.')

else:
	divisor_found = False
	 # test all possible divisors of n, from 2 to n - 1 (inclusive

	for d in range(2,n):
		if n % d == 0:	# we have just found a working divisor
			divisor_found = True 
			break 	# break leaves the loop 

	if divisor_found:	#same as divisor found == true
		print(f'{n} is not prime.')
	else:
		print(f'{n} is prime.')