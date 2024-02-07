'''
Home-brewed implementation of a map/dictionary.

Methods:

put(key, value) - Add a new key-value pair to the dictionary, or change the
 value associated with an existing key

get(key) - Return the value associated with key, or None if the key doesn't
 exist

delete(key) - Delete a key-value pair from the dictionary
'''

# This class represents a single key-value pair in the dictionary
class Entry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __str__(self):
		return f'<{self.key}, {self.value}>'


class MyOwnDictionary:
	def __init__(self):
		# Initially the hash table contains 5 indices
		# We resolve collisions with chaining, so each index is a list of
		#  Entry objects
		self.table = [ [] for i in range(5) ]

		# Can't use [[]] * 5 because that creates shallow copies of the lists
		#  (changing one will change them all)


	def __str__(self):
		result = ''
		for i in range(len(self.table)):	# For each index in the table...
			result += f'{i} - '
			for e in self.table[i]:			# For each entry at table[i]...
				result += str(e) + ' '
			result += '\n'
		return result


	# Hash function to use for the table
	# We assume the keys are strings
	def hash(self, key):
		return len(key) % len(self.table)


	def get(self, key):
		index = self.hash(key)

		# Search the list at table[index] for key, and return the
		#  corresponding value if found
		for e in self.table[index]:
			if e.key == key:
				return e.value

		# If we leave the loop without returning any value, the key must not
		#  exist in the list, and we can return None


	def delete(self, key):
		index = self.hash(key)

		# Search the list at table[index] for key, and delete that entry from
		#  the list if found
		for i in range(len(self.table[index])):
			if self.table[index][i].key == key:
				self.table[index].pop(i)
				return


	def put(self, key, value):
		index = self.hash(key)

		# Search the list at table[index] for key, and replace its value if
		#  found
		for e in self.table[index]:
			if e.key == key:
				e.value = value
				return

		# If we leave the loop without returning, the key must not exist in
		#  the list, so let's add a new entry with the key-value pair
		self.table[index].append(Entry(key, value))


	# Rehashes the table with the specified new_size
	def rehash(self, new_size):
		# Keep access to the old table
		old_table = self.table

		# Create the new table
		self.table = [ [] for i in range(new_size) ]

		# Go through all entries in the old table, and add them to the new
		#  table
		for r in old_table:
			for e in r:
				self.put(e.key, e.value)


if __name__ == '__main__':
	# Keys are movie names, values are year in which that movie was made
	data = MyOwnDictionary()

	# Tests for put
	data.put('Star Wars', 1977)
	data.put('MP and the HG', 1975)
	data.put('Jaws', 1975)
	data.put('Endgame', 2018)
	data.put('Dune', 2021)
	data.put('Tarzan', 1999)
	data.put('Mulan', 1998)
	print(data)

	data.put('Mulan', 2020)
	print(data)

	# Tests for get
	print(data.get('Mulan'))
	print(data.get('Dune'))
	print(data.get('Titanic'))

	# Tests for delete
	data.delete('Tarzan')
	print(data)
	data.delete('Jaws')
	print(data)

	# Test for rehash
	data.rehash(13)
	print(data)
