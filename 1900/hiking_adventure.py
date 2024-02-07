


def difficulty(t):

	for x in t:
		if 


			
	return t 


def print_difficulties(trail_list):

	for x in trail_list:
		difficulty = difficulty(trail_list)
		print(x,'-',{difficulty})


def easiest_trail(trail_list):
	difficulty = []
	for x in trail_list:
		difficulty.append(difficulty(trail_list))

	return min(difficulty)




trails = [ [500, 450, 500], [750, 1000, 900], [-150, -300, 0], [750, 1000, 900], [100, 200, 250] ]

print_difficulties(trails)
easiest_trail(trails)
