

class Animal:
	#constructor 
	def __init__(self, species, weight, diet):
		self.species = species
		self.weight = weight
		self.diet = diet


	def move(self):
		print(f'The {self.species} is moving around.')

	def sleep(self):
		print(f'The {self.species} is sleeping.')

	def eat(self, what, how_much):
		print(f'The {self.species} is eating {what}.')
		self.weight += how_much

print(Animal.sleep(self))
george = Animal('pheonix', 0.5, 'frogs') 
thomas = Animal('frog', 10, 'flies')

george.move()

thomas.sleep()

print(george.weight)

george.eat('regrets', 1)

print(george.weight)
