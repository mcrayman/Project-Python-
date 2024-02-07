'''
Some basic object-oriented programming (OOP) examples
'''

# The Animal class is a description/blueprint used to create Animal objects.
# Each Animal object has its own copy of the instance attributes/variables,
#  and it can call Animal's instance methods.

import random, sorting

class Animal:
	# count is a class attribute - this belongs to the Animal class as a
	#  whole, rather than to any Animal object/instance.  All Animal objects
	#  share the same value for a class attribute.
	count = 0

	# Constructor - an example of a Python "magic method"
	# Typically this is used to set values for the instance attributes, which
	#  are specified by adding self. in front of the variable name
	def __init__(self, species = 'crab', weight = 20, gender = 'null', is_cool = False):
		self.species = species
		self.weight = weight
		self.gender = gender
		self.is_cool = is_cool
		self.child = None	# This instance attribute keeps track of this
							#  Animal's child (created from __add__).  This is
							#  an example of a "has a" relationship.
		Animal.count += 1 	# ClassName.attribute accesses a class attribute

	# Another magic method.  __str__ controls how Animal objects should be
	#  represented as strings.  If this method isn't defined, Python defaults
	#  to showing the object's memory address.
	def __str__(self):
		return f'Animal object: species = {self.species}, weight = {self.weight}, gender = {self.gender}, is_cool = {self.is_cool}'

	# Another magic method.  __eq__ controls how Animal objects should be
	#  handled when using the == relational operator.  If __eq__ is not
	#  defined, == evaluates to True when the two variables are pointing to
	#  the same object in memory.
	def __eq__(self, other):
		# Here, we define __eq__ to return True if the Animal objects being
		#  compared share the same values for all instance attributes
		return self.species == other.species and self.weight == other.weight and self.gender == other.gender and self.is_cool == other.is_cool

	# Another magic method.  __lt__ controls how Animal objects should be
	#  handled when using the < relational operator.
	def __lt__(self, other):
		# Here, we define __lt__ to compare Animal objects by their weight
		return self.weight < other.weight

	# Another magic method.  __add__ controls how Animal objects should be
	#  handled when using the + operator.
	def __add__(self, other):
		# This method creates and returns a new Animal object with attributes
		#  based on the attributes of the two objects being added

		# The new species is made by combining the first half of self.species
		#  and the second half of other.species
		new_species = self.species[:len(self.species) // 2] + other.species[len(other.species) // 2:]

		# The new weight is the average of self.weight and other.weight
		new_weight = (self.weight + other.weight) / 2

		# The new gender is randomly selected
		new_gender = 'M' if random.randint(1, 2) == 1 else 'F'

		# The line above does the same thing as this:
		# if random.randint(1, 2) == 1
		# 	new_gender = 'M'
		# else:
		# 	new_gender = 'F'

		# The new animal is cool only if both self and other are cool
		new_is_cool = self.is_cool and other.is_cool

		# Create and return the new animal
		offspring = Animal(new_species, new_weight, new_gender, new_is_cool)

		# The new Animal object is assigned as the child of both self and other
		self.child = offspring
		other.child = offspring

		return offspring


	# Some other instance methods
	def move(self):
		print(f'The {self.species} is moving around.  Yaaay...')

	def sleep(self):
		print(f'The {self.species} is sleeping.  Zzzzz...')

	def eat(self, food, how_much = 0):
		if isinstance(food, Animal):	# Check if food is an Animal object
			print(f'The {self.species} is eating {food.species}.')
			self.weight += food.weight
		else:
			print(f'The {self.species} is eating {food}.')
			self.weight += how_much

	# Assumes that opponent is an Animal object
	def fight(self, opponent):
		print(f'The {self.species} is fighting vs. {opponent.species}.')
		if self.weight > opponent.weight:
			print(f'{self.species} wins!')
		else:
			print(f'{opponent.species} wins!')


# This conditional executes the code only if this is the file being run.  If
#  it's just being imported somewhere else, the code does not run.
if __name__ == '__main__':
	# Create some Animal objects and call their methods
	print(f'Animal.count = {Animal.count}')	# Shows 0
	slothington = Animal('pygmy three-toed sloth', 120, 'X', True)
	print(f'Animal.count = {Animal.count}')	# Shows 1
	slothington2 = Animal('pygmy three-toed sloth', 120, 'X', True)
	print(f'Animal.count = {Animal.count}')	# Shows 2
	slothington3 = slothington2
	print(f'Animal.count = {Animal.count}')	# Shows 2 - no new object was created
	hamza = Animal('Bulgarian tiger', 250, 'NB', True)
	print(f'Animal.count = {Animal.count}')	# Shows 3
	unicorn = Animal(is_cool = False, species = 'wabbajack')
	print(f'Animal.count = {Animal.count}')	# Shows 4

	# Shows None - neither slothington nor unicorn have called __add__ yet
	print(slothington.child)
	print(unicorn.child)

	# Call slothington.__add__(unicorn), and show the returned Animal object
	print(slothington + unicorn)

	# Shows the same Animal object as above, since __add__ assigned it as the
	#  child of both "parents"
	print(slothington.child)
	print(unicorn.child)
