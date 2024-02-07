'''
Implementation of a min-heap

We store the heap elements in a list.  For the node at index n in the list:
- the parent is at index (n - 1) // 2
- the left child is at index 2n + 1
- the right child is at index 2n + 2
'''

class MinHeap:
	def __init__(self):
		self.data = []	# List to store the heap elements

	def __str__(self):
		return str(self.data)

	# Adds new_data to the heap, swapping with the parent node as many times
	#  needed to maintain the min-heap property ("percolate up")
	def add(self, new_data):
		self.data.append(new_data)

		# Because the new element was just added to the end of the list, its
		#  index is the last index in the list
		child_index = len(self.data) - 1

		while True:
			# Recompute the parent index
			parent_index = (child_index - 1) // 2

			# If the child is smaller than the parent, swap the two
			if self.data[child_index] < self.data[parent_index]:
				self.data[child_index], self.data[parent_index] = self.data[parent_index], self.data[child_index]
				child_index = parent_index

				# Stop the loop if we've reached the root of the heap
				if child_index == 0:
					break

			# Stop the loop if the child is not less than the parent
			else:
				break


	# Removes and returns the top element from the heap	
	def delete(self):
		# TO BE WRITTEN in HW 4!


if __name__ == '__main__':
	m = MinHeap()

	# Test adding to an empty heap, and adding when no swaps are needed
	for i in [8, 11, 9, 24, 17, 50, 10]:
		m.add(i)
	print(m)

	# Test adding an element that requires swapping all the way up to the root
	m.add(2)
	print(m)

	# Test adding an element that requires 1 swap
	m.add(9)
	print(m)

	# Test adding an element that requires 2 swaps
	m.add(5)
	print(m)
