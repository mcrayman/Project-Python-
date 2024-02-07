'''
Examples of some sorting algorithms
'''

# Runs selection sort on the list x
# Summary of selection sort:
#  1) Find the min from the entire list x, and swap that with index 0
#  2) Find the min from x[1:], and swap that with index 1
#  3) Find the min from x[2:], and swap that with index 2
#  ... etc.
# Each iteration of this process correctly places 1 element.  Once we've
#  placed len(x) - 1 elements, the last element will automatically be in the
#  right place.  So we just need to run len(x) - 1 iterations.
def selection_sort(x):
	for j in range(len(x) - 1):	# Repeat len(x) - 1 times...
		# Find the min value from x[j:]
		min_index = j
		for i in range(j, len(x)):		
			if x[i] < x[min_index]:
				min_index = i

		# Swap the min value from above with x[j]
		x[j], x[min_index] = x[min_index], x[j]


# Runs insertion sort on the list x
# Summary of insertion sort:
#  1) Start by assuming x[0] is in the right place.  "Insert" x[1] by placing
#     it correctly relative to x[0].
#  2) "Insert" x[2] by placing it correctly relative to x[0] and x[1].
#  3) "Insert" x[3] by placing it correctly relative to x[0], x[1], and x[2].
#  ... etc.
# This process needs to be repeated for each of the len(x) - 1 elements after
#  the first one.
def insertion_sort(x):
	# j is the index of the element to insert.  We need to insert x[j]
	#  relative to the already-sorted portion of the list to its left.
	for j in range(1, len(x)):
		element_to_insert = x[j]

		# The while loop looks backward through the list to find the correct
		#  insertion point, shifting elements forward as it goes.  The i >= 0
		#  condition ensures that we don't go too far left in the list.
		i = j - 1
		while i >= 0 and x[i] > element_to_insert:
			x[i + 1] = x[i]
			i -= 1

		# Place the element to insert
		x[i + 1] = element_to_insert


test = [5, 3, 1, 8, 1, 2]
print(test)
selection_sort(test)
print(test)

test = [5, 3, 1, 8, 1, 2]
print(test)
insertion_sort(test)
print(test)
