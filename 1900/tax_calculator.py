'''
part A) When calculating a user's tax information, we first need to get the user's income 
by recieving input.Then calculating the amount of tax owed for each tax bracket  the user's 
income falls in ((income - previous tax bracket amount) * percent of tax). To determine total tax, 
add each tax bracket amount until the user has no more taxable income. (bracket1 * bracket 2...)
Finally, the effective tax rate is (total tax / income) * 100.
'''

# part B) this program determines a users tax information based on their income 

# get user income

income = float(input('What was your 2021 income? '))

# construct algorithm according to rules of tax bracket 

if 0 <= income <= 9950:
	tax = income * .1 
	
elif 9950 < income <= 40525:
	tax = (income - 9950) * .12 + 995 

elif 40525 < income <= 86375:
	tax = (income - 40525) * .22 + 995 + 3669

elif 86375 < income <= 164925:
	tax = (income - 86375) * .24 + 995 + 3669 + 10087
	
elif 164925 < income <= 209425:
	tax = (income - 164925) * .32 + 995 + 3669 + 10087 + 18852

elif 209425 < income <= 523600:
	tax = (income - 209425) * .35 + 995 + 3669 + 10087 + 18852 + 14240

elif 523600 < income:
	tax = (income - 523600) * .37 + 995 + 3669 + 10087 + 18852 + 14240 + 109961.25
	
# output tax owed and effective tax rate 

print(f'Total tax owed:  ${tax:.2f}')

rate = (tax / income) * 100

print(f'Effective tax rate: {rate:.1f}%')

