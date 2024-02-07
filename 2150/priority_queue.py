'''
Uses our MinHeap class to implement a priority queue.  In a priority queue,
the highest-priority element is always the first one to be removed.  Since
we're storing the elements in a min-heap, the "smallest" element is
considered the highest priority one.  Using a heap allows both enqueue
and dequeue to be O(log n) operations.
'''

from min_heap import MinHeap

class PriorityQueue:
	def __init__(self):
		# PriorityQueue has one instance attribute: a MinHeap object
		# (This is known as a "has-a" relationship)
		self.internal_heap = MinHeap()

	def __str__(self):
		return str(self.internal_heap)

	# To add an element to the PriorityQueue, just delegate the work to
	#  MinHeap's add method
	def enqueue(self, new_data):
		self.internal_heap.add(new_data)

	# Once MinHeap has a delete method defined, we could delegate dequeue
	#  similarly


if __name__ == '__main__':
	pq = PriorityQueue()
	for e in ['waffles', 'french toast', 'eggs', 'syrup', 'sausage', 'bacon', 'cereal']:
		pq.enqueue(e)

	print(pq)
