
def pizza_cost(size):	#header
	if size == 'S':
		cost = 4.99
	elif size == 'M':
		cost = 30
	elif size == 'L':
		cost = 10
	else:
		cost = 50
	return cost 

def pizza_cost_better(size, num_toppings):
	if size == 'S':
		cost = 4.99
		cost_per_topping = 1
	elif size == 'M':
		cost = 30
		cost_per_topping = 2.50
	elif size == 'L':
		cost = 10
		cost_per_topping = 15
	else:
		cost = 50
		cost_per_topping = 13
	return cost + cost_per_topping * num_toppings


# calling (invoking) the function
print(pizza_cost('S'))
price = pizza_cost('M')
print(price)
order_price = 30 * pizza_cost('L') + 13 * pizza_cost('F')
print(order_price)

print(pizza_cost_better('F', 24))

#get user input for pizza size and number of toppings 
pizza_size = input('How big do you want your pizza? ')
t = int(input('How many toppings? '))

print(pizza_cost_better(pizza_size,t))

c = pizza_cost_better(pizza_size, pizza_cost('M'))
print(c)





