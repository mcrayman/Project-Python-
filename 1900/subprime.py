
#this program uses algorithms to respond to a canceled customer with their refund amount and goodbye message

#filters out leap years 
def days_in_year(y):
    return (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0)

#determines amount of days in each month
def days_in_month(m,y):
	if m in [4, 6, 9, 11]:
		daysm = 30
	elif m in [1, 3, 5, 7, 8, 10, 12]:
		daysm = 31        
	elif m == 2 and days_in_year(y) == True:
		daysm = 29
	elif m == 2 and days_in_year(y) == False:
		daysm =  28
	else:
		return none
	
   #this algorithm determines how many days left in the year and the amount of refund to give
def days_left_in_year(m,d,y):
	total_days = 0
	m -= 1
	while m > 0:
		if m in [4, 6, 9, 11]:
			daysm = 30
		elif m in [1, 3, 5, 7, 8, 10, 12]:
			daysm = 31        
		elif m == 2 and days_in_year(y) == True:
			daysm = 29
		elif m == 2 and days_in_year(y) == False:
			daysm =  28
		else:
			return none
		total_days += daysm
		m -= 1
	total_days += d
	if days_in_year(y) == True:
		total = 366
	if days_in_year(y) == False:
		total = 365
	days_left = total - total_days
	refund = days_left / total * 278
	print(f'Ok, you’ll be issued a prorated refund of ${refund:.2f}.')

#This asks user for date of canceled subscription

print('When did you cancel your Subprime service? ')
days_left_in_year(int(input('Month: ')),int(input('Day: ')),int(input('Year: ')))

print('Thanks for using Subprime - disappointing customers is our priority!')