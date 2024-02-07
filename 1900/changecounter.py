'''
this program determines a combination of us coins that adds up to a cerain # of cents
'''

# get user input for the number of cents

cents = int(input('How many cents?'))

# figure out how many quartes, dimes, nickels, and pennies fit into that amount

num_quarters = cents // 25
num_dimes = cents % 25 // 10
num_nickels = cents % 25 % 10 // 5
num_pennies =  cents % 25 % 10 % 5 // 1

# show results on screen

print(num_quarters, 'quarters')
print(num_dimes, 'dimes')
print(num_nickels, 'nickels')
print(num_pennies, 'pennies')