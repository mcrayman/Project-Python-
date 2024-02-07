
#example of search algorithms

import time

def linear_search(stuff, target):
	for i in range(len(stuff)):
		if stuff[i] == target:
			return i
	return -1


def linear_search_rec(stuff, target, current_index):
	if stuff == []:
		return -1
	elif stuff[0] == target:
		return current_index
	else:
		return linear_search_rec(stuff[1:], target, current_index + 1)
		 

def binary_search(stuff, target):
	lower = 0
	upper = len(stuff) - 1
	while lower <= upper:
		mid_index = (lower + upper) // 2
		if stuff[mid_index] == target:
			return mid_index
		elif stuff[mid_index] > target:
			upper = mid_index - 1
		else:
			lower = mid_index + 1
	return -1

data = [-7, 3, 4, 6, 10, 14]

print(linear_search_rec(data, 6, 0))
print(linear_search_rec(data, 0, 0))

'''
data = [1,2,3,4,13,-5,10]
for d in data:
	print(linear_search(data, d))
print(linear_search(data, 12))
print(linear_search(data, 0))

data_sorted = [-7, 3, 4, 6, 10, 14]
for d in data_sorted:
	print(binary_search(data_sorted, d))
print(binary_search(data_sorted, -10))
print(binary_search(data_sorted, 10))
'''
'''
size = 30000000
target = size - 1
large_list = [i for i in range(size)]
start_time = time.process_time()

print(linear_search(large_list, target))
end_time = time.process_time()
print(f'Linear search took {(end_time - start_time):.3f} seconds')

start_time = time.process_time()
print(binary_search(large_list, target))
end_time = time.process_time()
print(f'Binary search took {(end_time - start_time):.3f} seconds')
'''









