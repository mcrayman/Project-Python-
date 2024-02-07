'''
Implementation of a queue using a singly linked list.  A queue is an abstract
data type (ADT) that supports three main operations:

- enqueue: add a new element to the back of the queue
- dequeue: remove and return the front element
- peek: return the front element, without removing

Note that we interact with the queue from both ends (front and back).

We use the head of the list as the front of the queue, and we maintain a tail
reference on the list to keep track of the back of the queue.
'''

class Node:
	def __init__(self, data, next_node):
		self.data = data
		self.next = next_node

class LLQueue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __str__(self):
		result = 'LLQueue (front to back): '
		temp = self.head
		while temp != None:
			result += str(temp.data) + ' '
			temp = temp.next
		return result

	def peek(self):
		# Return the data at the front of the queue (head of the list)
		if self.size > 0:
			return self.head.data
		# Returns None if the queue is empty

	def dequeue(self):
		# Remove and return the data at the front of the queue (head of the
		#  list)
		if self.size > 0:
			temp = self.head.data

			self.head = self.head.next
			self.size -= 1

			# If the removal emptied the queue, update the tail reference
			if self.size == 0:
				self.tail = None

			return temp
		# Returns None if the queue is empty

	def enqueue(self, new_data):
		# Add a new node to the tail of the list

		# Start by creating a new Node object
		new_node = Node(new_data, None)

		# Special case of adding to an empty queue - the new node becomes both
		#  the head and tail of the list
		if self.size == 0:
			self.head = self.tail = new_node

		# Adding to a non-empty queue - the new node is added after the tail
		#  node, and we update the tail reference
		else:
			self.tail.next = new_node
			self.tail = self.tail.next

		self.size += 1


if __name__ == '__main__':
	q = LLQueue()
	print(q)

	for i in range(5):
		q.enqueue(i)
		print(q)

	while q.size != 0:
		print(f'peek returned {q.peek()}, queue = {q}')
		print(f'dequeue returned {q.dequeue()}, queue = {q}')
