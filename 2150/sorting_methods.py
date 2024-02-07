
#Examples of sorting lists

#1
import sorting_methods

def selection_sort(x):
	for j in range(len(x) - 1):
		min_index = j
		for i in range(j, len(x)):
			if x[i] < x[min_index]:
				min_index = i


		x[j], x[min_index] = x[min_index], x[j]


#2

def insertion_sort(x):
	for j in range(1, len(x)):
		#insert x[i] relative to the already sorted portion to its left
		element_to_insert = x[j]
		i = j - 1
		while i >= 0 and x[i] > element_to_insert:
			x[i + 1] = x[i]
			i -= 1
		x[i + 1] = element_to_insert

test = [5,3,1,8,1,2]

print(test)
insertion_sort(test)
print(test)
print()

test = [5,3,1,8,1,2]

print(test)
selection_sort(test)
print(test)
