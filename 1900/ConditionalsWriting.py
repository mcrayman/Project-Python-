# 2 points, 1 for effort. Maximum attempts: 2.

'''
A leap year is a year in which February has 29 days instead of 28.
There are two ways for a year to be a leap year:

1) The year is divisible by 400.

2) The year is divisible by 4, but *not* a multiple of 100.

Examples:
- 2000 was a leap year (divisible by 400)
- 2020 was a leap year (divisible by 4, not a multiple of 100)
- 2100 will *not* be a leap year (divisible by 4, but *is* a multiple of 100)

Complete the program below, which should print if the year entered by the
user is a leap year or not.
'''

year = int(input('Enter a year: '))

if year % 400 == 0:
	print(year, 'is a leap year.')

elif year % 100 == 0:
	print(year, ' is not a leap year')

elif year % 4 == 0:
	print(year, 'is a leap year.')
	

	

	



	 



