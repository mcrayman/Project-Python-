n = int(input('How many numbers do you want to enter? '))
while n < 2:  # COMPLETE THIS BLANK
	n = int(input('Must enter at least 2 numbers!  Try again: '))

total = 0
i = 1
while i <= n:	# Run n iterations...
	next_number = float(input(f'Enter number {i}: '))

	# Update lowest_number
	if i == 1 or next_number < lowest_number:  # COMPLETE THIS BLANK
		lowest_number = next_number

	# Update total
	total += next_number

	i += 1

# Compute the average
avg = total / n

# Compute the average excluding the lowest number
total_without_lowest = total - lowest_number   # COMPLETE THIS BLANK
qty_without_lowest = n - 1    # COMPLETE THIS BLANK
avg_without_lowest = total_without_lowest / qty_without_lowest

# Show results
print(f'Average: {avg}')
print(f'Average without lowest: {avg_without_lowest}')
