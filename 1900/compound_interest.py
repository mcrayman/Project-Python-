#simulation of how money grows when compounded annually

initital_deposit = float(input('Enter initial deposit, in dollars: '))
interest_rate = float(input('Enter interest rate, as a percentage: '))
extra_amount = float(input('Enter extra annual contribution, in dollars: '))
num_years = int(input('How many years? '))

balance_start = initital_deposit

i = 1
while i <= num_years:
	interest_paid = balance_start * interest_rate / 100 
	balance_end = balance_start + interest_paid + extra_amount
	print(f'{i}\t${balance_start:12.2f}\t${interest_paid:12.2f}\t${extra_amount:12.2f}\t${balance_end:12.2f}')
	balance_start = balance_end 
	i += 1
