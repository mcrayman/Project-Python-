'''
Implementation of a stack using a singly linked list.  A stack is an abstract
data type (ADT) that supports three main operations:

- push: add a new element to the top of the stack
- pop: remove and return the top element
- peek: return the top element, without removing

Note that we interact with the stack *only* from the top!

We use the head of the list as the top of the stack, since this gives us easy
access for all stack operations.
'''

class Node:
	def __init__(self, data, next_node):
		self.data = data
		self.next = next_node

class LLStack:
	def __init__(self):
		self.head = None
		self.size = 0

	def __str__(self):
		result = 'LLStack (top to bottom): '
		temp = self.head
		while temp != None:
			result += str(temp.data) + ' '
			temp = temp.next
		return result

	def push(self, new_data):
		# Add a new node containing new_data to the head of the list
		self.head = Node(new_data, self.head)
		self.size += 1

	def pop(self):
		if self.size > 0:
			# Store the value to return
			result = self.head.data

			# Remove the head node from the list
			self.head = self.head.next

			self.size -= 1
			return result
		# Returns None if called with an empty stack

	def peek(self):
		if self.size > 0:
			return self.head.data
		# Returns None if called with an empty stack


if __name__ == '__main__':
	s = LLStack()
	print(s)

	for e in ['this', 'is', 'so', 'fun']:
		s.push(e)
		print(s)

	while s.size != 0:
		print(f'peek returned {s.peek()}, stack = {s}')
		print(f'pop returned {s.pop()}, stack = {s}')
