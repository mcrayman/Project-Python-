# This import syntax lets us use Animal without saying animal.Animal
from animal import Animal

# Sloth is a subclass of Animal - it inherits the components of Animal without
#  having to redefine them.  Animal is known as a superclass of Sloth.
# Some synonyms for subclass/superclass: child class/parent class, derived
#  class/base class
class Sloth(Animal):
	# The Sloth constructor needs just weight, gender, climbing_speed
	def __init__(self, weight, gender, climbing_speed):
		# We call the Animal constructor to set the first four instance
		#  attributes (species, weight, gender, is_cool).  All Sloth objects
		#  have a species of 'sloth' and an is_cool value of True.
		Animal.__init__(self, 'sloth', weight, gender, True)

		# Sloth objects also add a new instance attribute for climbing_speed
		self.climbing_speed = climbing_speed

	# Overrides the __str__ method of Animal.  When a Sloth object calls
	#  __str__, it uses this version instead of the one inherited from Animal.
	def __str__(self):
		# First we call Animal's __str__, then we add some info about
		#  climbing_speed and then replace Animal with Sloth
		result = Animal.__str__(self) + f', climbing_speed = {self.climbing_speed}'
		return 'Sloth' + result[6:]

	# Overrides the move method inherited from Animal - whenever a Sloth object
	#  calls move, it calls the climb method
	def move(self):
		self.climb()

	# A new instance method that's specific to Sloth objects
	def climb(self):
		print('This sloth is climbing to the top of the Animal hierarchy, where it belongs.')


# A subclass of Sloth
class PygmyTTSloth(Sloth):
	# Even if the subclass makes no changes or additions to the superclass,
	#  Python doesn't allow an empty class.  We can just use pass.
	pass

# This conditional executes the code only if this is the file being run.  If
#  it's just being imported somewhere else, the code does not run.
if __name__ == '__main__':
	flash = Sloth(25, 'M', 0.0003)
	print(flash)
	flash.climb()	# climb is defined in Sloth
	flash.sleep()	# sleep is inherited from Animal
	flash.move()	# move is inherited from Animal and overridden in Sloth

	flash.climbing_speed = 0.004
	print(flash)

	flash_jr = PygmyTTSloth(2, 'F', 0.0002)	# Calls Sloth's __init__ method
	print(isinstance(flash, Sloth))		# True
	print(isinstance(flash, Animal))	# A Sloth "is an" Animal - True
	print(isinstance(flash_jr, PygmyTTSloth))	# True
	print(isinstance(flash_jr, Sloth))	# A PygmyTTSloth "is a" Sloth - True
	print(isinstance(flash_jr, Animal))	# A PygmyTTSloth "is a" Sloth, which
										#  "is an" Animal - True
