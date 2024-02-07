# finds highest value of set of numbers

#get user input for how many numbers 

n = int(input('How many numbers?'))
while n <= 0:
	n = int(input('Invalid value! Try again: '))


highest = 0

# loop that runs n iterations
i = 0 
while i < n:
	# get input for next number 
	next_num = float(input('Enter the next number: '))

	# on the first iteration, initialize highest to the first number
	# on later interations replace highest if next_num is higher 
	if i == 0 or next_num > highest:
		highest = next_num

	i += 1

print(f'The highest is: {highest}')