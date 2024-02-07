import random


num = int(input('How many numbers?: '))

i = 1
while i < num:
	card_num = '4'

	num_length = 13 + 3 * random.randint(0,2)

	for i in range(num_length - 2):
		card_num += str(random.randint(0,9))

	luhn_sum = 0

	for i in range(num_length - 2, -1, -2):
		this_digit = int(card_num[i])
		this_digit *= 2
		if this_digit > 9:
			this_digit -= 9
		luhn_sum += this_digit

	for i in range(num_length - 3, -1, -2):
		this_digit = int(card_num[i])
		luhn_sum += this_digit

	ones_digit = luhn_sum % 10

	last_digit = (10 - ones_digit) % 10

	card_num += str(last_digit)
	print(card_num)
	i = i + 1

#get user input

#stop loop 