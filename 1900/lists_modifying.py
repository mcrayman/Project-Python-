#using loops to access / change elements of a list

#we want to replace all negative values with 0


def elements_to_0(data):
	for i in range(len(data)): # use this to change elements of a list 
		if data[i] < 0:
			data[i] = 0

data = [14,12,3,-14,-9,7]
print(data)
elements_to_0(data)
print(data)



def replace_negatives_with_zero(x):
	for i in range(len(x)):
		if x[i] < 0:
			x[i] = 0 
		
x = [11, 14, 13, -7, -12,-42,8]
replace_negatives_with_zero(x)
print(x)


def capitalize_names(x):
	for i in range(len(x)):
		this_name = x[i]
		if 'a' <= this_name[0] <= 'z':
			new_name = this_name[0].upper() + this_name[1:]
			x[i] = new_name


names = ['addison', 'bartholomeu', 'candice', 'delores']
print(names)
capitalize_names(names)
print(names)

def add_1_to_odds(x):
	for i in range(len(x)):
		if x[i] % 2 != 0:
			x[i] += 1

x = [11, 14, 13, -7, -12, -42, 8]
add_1_to_odds(x)
print(x)


def remove_all_negatives(x):
	i = 0
	while i < len(x):
		if x[i] < 0:
			x.remove(x[i])
		else:
			i += 1


x = [11, 14, 13, -7, -12, -42, 8]
print(x)
remove_all_negatives(x)
print(x)


#returns a list that excludes all negative values from x, does not modify original list
def remove_all_negatives_with_return(x):
	new_list = []
	for i in x:
		if i >= 0:
			new_list.append(i)
	return new_list

x = [11, 14, 13, -7, -12, -42, 8]
print(x)
result = remove_all_negatives_with_return(x)
print(result)




































