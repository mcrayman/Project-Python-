
#Sorting methods

#1

def find_min_and_index(x):
	min_element = x[0]
	curr_index = 0
	min_index = 0
	for i in x:
		if i < min_element:
			min_element = i
			min_index = curr_index
		curr_index += 1
	print(f'Min is {min_element}')
	print(f'Index of min is {min_index}')


#2 

def find_min_and_index_v2(x):
	min_element = x[0]
	min_index = 0
	for i in range(len(x)):
		if x[i] < min_element:
			min_element = x[i]
			min_index = i 

	print(f'Min is {min_element}')
	print(f'Index of min is {min_index}')


#3

def find_min_and_index_v3(x):
	min_index = 0
	for i in range(len(x)):
		if x[i] < x[min_index]:
			min_index = i 
	print(f'Min is {min_index}')
	print(f'Index of min is {min_index}')


test = [5,3,1,0,1,2]
find_min_and_index(test)
find_min_and_index_v2(test)
find_min_and_index_v3(test)