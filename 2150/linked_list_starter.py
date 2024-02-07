'''
Starter code for HW 3, Problem 1

Defines a class for one node of a linked list and a class for a linked list
'''
import random
class Node:
	def __init__(self, data, next_node):
		self.data = data
		self.next = next_node

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def __str__(self):
		result = 'head -> '
		temp = self.head
		while temp != None:
			result = result + str(temp.data) + ' -> '
			temp = temp.next
		result += 'None'
		return result


	# Returns the list node at the specified index, or None if the index is
	#  invalid.  Caution: this should return the Node *object*, not the data
	#  contained within!
	def node_at_index(self, index):
		if 0 <= index < self.size:
			curr_idx = 0
			temp = self.head
			while curr_idx <= index:
				if curr_idx == index:
					return temp
				temp = temp.next
				curr_idx += 1
		else:
			return None

	# Returns the element at the specified index of the list, or None if
	#  the index is invalid
	def get_element_at_index(self, index):
		if 0 <= index < self.size:
			return self.node_at_index(index).data
		else:
			return None

	# Changes the element at the specified index of the list to new_value.
	#  Does nothing if the index is invalid.
	def set_element_at_index(self, index, new_value):
		if 0 <= index < self.size:
			self.node_at_index(index).data = new_value


	# Adds a new node containing new_data at the specified index.  Does nothing
	#  if the index is invalid.
	def add_at_index(self, new_data, index):
		if 0 <= index <= self.size:
			# Special case for inserting at index 0 (head of list)
			if index == 0:
				self.head = Node(new_data, self.head)
			# Insert at other list indices
			else:
				node_before = self.node_at_index(index - 1)
				node_before.next = Node(new_data, node_before.next)

		self.size += 1

	# Removes the node at the specified index from the list.  Does nothing if
	#  the index is invalid.
	def delete_at_index(self, index):
		if 0 <= index <= self.size:
			if index == 0:
				self.head = self.head.next
			else:
				self.node_at_index(index - 1).next = self.node_at_index(index + 1)

		self.size -= 1



if __name__ == '__main__':
	my_list = LinkedList()
	print(my_list)

	my_list.add_at_index(1, 0)
	print(my_list)
	my_list.add_at_index(2, 0)
	print(my_list)
	my_list.delete_at_index(1)
	print(my_list)
	my_list.add_at_index(1, 1)
	print(my_list)
	my_list.add_at_index(3, 0)
	print(my_list)
	my_list.add_at_index(4, 2)
	print(my_list)
	my_list.add_at_index(5, my_list.size - 1)
	print(my_list)
	my_list.add_at_index(6, my_list.size)
	print(my_list)
	my_list.add_at_index(7, -2)
	print(my_list)
	my_list.delete_at_index(0)
	print(my_list)
	my_list.delete_at_index(2)
	print(my_list)
	my_list.delete_at_index(my_list.size - 2)
	print(my_list)
	my_list.delete_at_index(6)
	print(my_list)
	print()

	my_list = LinkedList()
	print(my_list)
	my_list.add_at_index(1, 0)
	print(my_list)
	my_list.delete_at_index(0)
	print(my_list)

