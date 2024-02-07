# this program lists all the primes within a cerain range


def is_prime(n):
	if n >= 2:
		divisor_found = False
		 # test all possible divisors of n, from 2 to n - 1 (inclusive

		for d in range(2,n):
			if n % d == 0:	# we have just found a working divisor
				divisor_found = True 
				break 	# break leaves the loop 
	
		return not divisor_found 
	else:
		return False

def list_primes(start,end):
	for n in range(start, end + 1):
		if is_prime(n) == True:
			print(n)
		
start = int(input('Enter start point: '))
end = int(input('Enter end point: '))


list_primes(start,end)

