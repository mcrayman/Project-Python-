

print('Please enter the following information:')

p = float(input('Initial amount of loan:'))

ann_int = float(input('Annual interest rate (in %):'))

num_years = float(input('Number of years:'))

r = (ann_int / 12) / 100

n = num_years * 12

m = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

tp = m * n 

i = tp - p

print(f'Monthly payment: ${m:.2f}')
print(f'Total paid:      ${tp:.2f}')
print(f'Interest paid:   ${i:.2f}')