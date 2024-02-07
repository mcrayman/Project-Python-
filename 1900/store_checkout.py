'''
this program simulates checkout from an online store that sells three types of items
'''
price_headphones = 100
price_water = 9.99
price_sloths = 10000



# variables to store quantities of each item 

qty_headphobnes = int(input('How many headphones?'))
qty_water = int(input('How many waters?'))
qty_sloths = int(input('How many sloths?'))


subtotal = price_headphones * qty_headphobnes + price_water * \
qty_water + price_sloths * qty_sloths

#compute the amount of tax (9.75) 
# compute final total 

tax = subtotal * .0975
final_total = tax + subtotal

print(subtotal)
print('tax: ' + str(tax))
print('Total: ', final_total)

