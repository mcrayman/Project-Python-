


weeks = int(input('How many weeks of data do you have? '))

if weeks < 2:
	weeks = int(input('Must enter at least 2 weeks, try again: '))


mileage = []
for i in range(weeks):
	miles = float(input('Enter miles run for week {}: '.format(i + 1)))
	if miles < 0:
		miles = float(input('You can’t run a negative number of miles, try again: '))
	mileage.append(miles)


increasing = True
avg = 0
for i in range(1, weeks):
    if mileage[i - 1] > mileage[i]:
        increasing = False
    avg += mileage[i] - mileage[i - 1]

avg /= (weeks - 1)

if increasing:
    print("Your weekly mileage is consistently increasing!")
else:
    print("Your weekly mileage is NOT consistently increasing!")
    
print("Average weekly change:", avg)