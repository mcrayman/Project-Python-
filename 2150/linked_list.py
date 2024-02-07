'''
Defines a class for one node of a linked list and a class for a linked list
'''

class Node:
	# Each Node object contains some data, and a reference to the next node
	def __init__(self, data, next_node):
		self.data = data
		self.next = next_node

class LinkedList:
	# The linked list must maintain a reference to its head (first) node
	def __init__(self):
		# The list is empty when first created, so its head points to None
		self.head = None

		# The size attribute keeps track of how many nodes are in the list
		self.size = 0

	# The __str__ method performs a list traversal
	# Start by making a new reference (temp) that points to the head node, then
	#  move that reference down the list one node at a time
	def __str__(self):
		result = 'head -> '
		temp = self.head 	# temp points to the same Node object as head
		while temp != None:	# Keep going as long as temp points to a Node
			result = result + str(temp.data) + ' -> '
			temp = temp.next # Move temp to the following node
		result += 'None'
		return result

	# Adds a new node containing new_data at the specified index.  Does nothing
	#  if the index is invalid.
	def add_at_index(self, new_data, index):
		# Check for valid index
		# Note that self.size *is* considered a valid index - this means add
		#  after the tail of the list
		if 0 <= index <= self.size:
			# Special case for inserting at index 0 (head of list)
			if index == 0:
				# Same as the add_to_head method we had before
				self.head = Node(new_data, self.head)

			# Insert at other list indices
			else:
				# Get to the node at (index - 1) in the list
				node_before = self.head
				for i in range(index - 1):
					node_before = node_before.next

				# Create the new node to insert, and connect it to the list
				node_before.next = Node(new_data, node_before.next)

			# Update the size attribute, since we just added a new node
			self.size += 1

	# Removes a node from the head of the list
	def delete_from_head(self):
		if self.head != None:	# Make sure there is a node to remove!
			self.head = self.head.next	

			# Update the size attribute, since we just removed a node
			self.size -= 1

	# Returns the element at the specified index of the list, or None if
	#  the index is invalid
	def get_element_at_index(self, index):
		# Check for valid index
		if 0 <= index < self.size:
			# Get to the node at the index
			temp = self.head
			for i in range(index):
				temp = temp.next

			# Return the data within the node at that index
			return temp.data

	# Changes the element at the specified index of the list to new_value.
	#  Does nothing if the index is invalid.
	def set_element_at_index(self, index, new_value):
		# Check for valid index
		if 0 <= index < self.size:
			# Get to the node at the index
			temp = self.head
			for i in range(index):
				temp = temp.next

			# Change temp's data to be new_value
			temp.data = new_value


if __name__ == '__main__':
	# Create a new empty list
	stuff = LinkedList()
	print(stuff)

	# Add some elements
	for i in range(5):
		stuff.add_at_index(i, 0)
		print(stuff)

	# Get the individual elements from the list
	for i in range(stuff.size):
		print(stuff.get_element_at_index(i))

	# Change the list's elements
	for i in range(stuff.size):
		stuff.set_element_at_index(i, stuff.get_element_at_index(i) + 1)

	print(stuff)
