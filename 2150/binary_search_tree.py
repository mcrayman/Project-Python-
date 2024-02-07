'''
Implementation of a binary search tree (BST).

A BST is a binary tree where every node satisfies the condition of being >=
all nodes in its left subtree, and <= all nodes in its right subtree.
'''
import random
from random import randint
# Each node of the tree stores data, a left child, and a right child.
# The children are initialized to None when the node is first created.
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinarySearchTree:
	# The tree keeps track of its root node.  An empty tree has root pointing
	#  to None.
	def __init__(self):
		self.root = None
		self.parent = None


	# Returns a visual representation of the tree
	# (This is essentially a wrapper for the recursive show_tree method)
	def __str__(self):
		return self.show_tree(self.root, '')

	# This method returns a visual representation of the subtree whose root is
	#  at where.  The indent parameter keeps track of how much to indent each
	#  level.
	def show_tree(self, where, indent):
		# Base case
		if where == None:
			return indent + 'None'
		else:
			# The backslash at the end of these lines tells Python to continue
			#  the code on the following line - useful for making long
			#  expressions more readable
			return indent + str(where.data) + '\n' +\
				self.show_tree(where.left, indent + '_') + '\n' +\
				self.show_tree(where.right, indent + '_')


	# Wrapper method for an in-order traversal - this just calls the recursive
	#  helper method starting from the root of the tree
	def in_order_traversal(self):
		print('In-order traversal:')
		self.in_order_traversal_helper(self.root)

	# Recursive helper method for in-order traversal
	def in_order_traversal_helper(self, where):
		# Base case is when where == None, in this case do nothing
		if where != None:
			self.in_order_traversal_helper(where.left)
			print(where.data)
			self.in_order_traversal_helper(where.right)


	# Add new_data to the tree
	def add(self, new_data):
		# Create a new Node object containing new_data
		new_node = Node(new_data)

		# If the tree is empty, make new_node the root
		if self.root == None:
			self.root = new_node

		# If the tree is not empty, start from the root and search down the
		#  tree until an available spot is found		
		else:
			temp = self.root
			am_i_done = False

			while not am_i_done:
				if new_data < temp.data:
					# Go left
					if temp.left == None:		# Open space on temp's left -
						temp.left = new_node	#  add new_node there
						am_i_done = True
					else:
						temp = temp.left
				else:
					# Go right
					if temp.right == None:		# Open space on temp's right -
						temp.right = new_node	#  add new_node there
						am_i_done = True
					else:
						temp = temp.right


	# Searches the tree for a target.  Returns the target from the tree if it
	#  exists, or None if the target doesn't exist.
	# This is a wrapper for the recursive get_helper below.
	def get(self, target):
		return self.get_helper(target, self.root)

	# Searches the subtree whose root is where for the target.
	# Returns the target if it exists in that subtree, or None of the target
	#  doesn't exist.
	def get_helper(self, target, where):
		# Base case - the target can't exist in an empty subtree
		if where == None:
			return None

		# Compare target vs. where.data, and use the result to recursively
		#  search left or right

		# Base case - target found!
		if target == where.data:
			return where.data
		elif target < where.data:
			return self.get_helper(target, where.left)
		else:
			return self.get_helper(target, where.right)

	def traverse_bst(self, where):
		root = self.root
		if root == None:
			return None

		while root.data != where:
			if root.data > where:
				root = root.left
			elif root.data < where:
				root = root.right

		return root

	def delete_predecessor(self, where):
		root = self.traverse_bst(where)

		if not root.left:
			return None

		root = root.left
		while root.right:
			self.parent = root
			temp = root
			root = root.right

		self.parent = None
		return temp.data



	def delete_successor(self, where):
		root = self.traverse_bst(where)
		if not root.right:
			return None

		root = root.right
		while root.left:
			self.parent = root
			temp = root
			root = root.left

		self.parent = None
		return temp.data

	def delete(self, target):
		root = self.traverse_bst(target)

		if not root.left and not root.right:
			temp = root.data
			root.data = None
			return temp

		if not root.left and root.right:
			temp = root.data
			root = root.right
			return temp

		if not root.right and root.left:
			temp = root.data
			root = root.left
			return temp

		num = random.randint(0,1)
		if num == 1:
			node = self.delete_successor(root.data)
		else:
			node = self.delete_predecessor(root.data)

		temp = root.data
		root = node
		return temp

	def height(self):
		root = self.root
		if root == None:
			return 0

		height = 0
		done = False
		while not done:
			if root.left:
				root = root.left
				height += 1
			if root.right:
				root = root.right
				height += 1
			if root.right == None and root.left == None:
				done = True

		return height

	def level_order_traversal(self):
		root = self.root
		if root is None:
			return None

		queue = []
		queue.append(root)

		while len(queue) > 0:
			print(queue[0].data)

			node = queue.pop(0)

			if node.left:
				queue.append(node.left)

			if node.right:
				queue.append(node.right)

	def foo(self):
		temp = self.root
		while temp != None and temp.left != None:
			temp = temp.left
		return temp.data

if __name__ == '__main__':
	t = BinarySearchTree()

	for e in [-9, 20, 2, 4, 15, -6, 10]:
		t.add(e)

	print(t.in_order_traversal())
	print(t.foo())