# heres proof you shoudl not take this deal

todays_amount = 0.01
total = 0

i = 1
while i < 31:
	total = total + todays_amount
	print(f'Day {i}: ${todays_amount:.2f} Total so far: ${total:.2f}')
	todays_amount *= 2
	i += 1