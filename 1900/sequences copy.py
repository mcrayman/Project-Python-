# this program runs sequences of numbers from algorithm 

term = 1443

num = 1

print('Part (a)')
# takes term and adds 4
i = 0
while i < 96:
	print(num,'\b.', term)
	num += 1
	term += 4
	i += 1 

term = 100.0

num = 1

print(' ')
print('Part (b)')
#takes term and adds 10%
i = 0
while i < 50:
	print(num,'\b.', term)
	num += 1
	term = term + (term * .1)
	i += 1 

term = 370

num = 1
pop = 1 

print(' ')
print('Part (c)')
#takes term and increments by term + 1
i = 0
while i < 73:
	print(num,'\b.', term)
	num += 1
	inc = pop
	term = term + inc
	pop += 2
	i += 1 
#----------------------------
term1 = 11
term2 = 8
term3 = 14
term4 = term1 + term2 + term3 

num = 1

print(' ')
print('Part (d)')
#takes 3 previous term's sum for 4th term, continuously
while num <= 42:
	print(num,'\b.', term1)
	term1 = term2 + term3 + term4
	num += 1
	print(num,'\b.', term2)
	term2 = term3 + term4 + term1
	num += 1
	print(num,'\b.', term3)
	term3 = term4 + term2 + term1
	num += 1
	print(num,'\b.', term4)
	term4 = term3 + term2 + term1
	num += 1
	
term = 777

num = 1

print(' ')
print('Part (e)')
# determines whether term is even or odd using, then 'if' statements to change variable 
i = 1
while i < 38:
	print(num,'\b.', term)
	if term % 2 == 0:
		term //= 2
	elif term % 2 != 0:
		term = 3 * term + 1
	i += 1
	num += 1
	




