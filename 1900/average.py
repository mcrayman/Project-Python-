# finds average of set of numbers

#get user input for how many numbers 

n = int(input('How many numbers?'))
while n <= 0:
	n = int(input('Invalid value! Try again: '))


total = 0

# loop that runs n iterations
i = 0 
while i < n:
	# get input for next number 
	next_num = float(input('Enter the next number: '))
	total += next_num
	i += 1

avg = total / n
print(f'The averaage is: {avg}')