
#define class Car
class Car:
	#initialize constructor
	def __init__(self, make, model, color, price): 

		self.mileage = 0

		self.make = make
		self.model = model
		self.color = color
		self.price = price

	def set_price(self, p):

		self.price += p

	def paint(self, c):

		self.color = c

	def show_car_info(self):

		print(self.make, self.model, self.color, self.price)
		
	def travel(self, distance):

		self.distance = mileage

#Give __init__ parameters values
car1 = Car('Porsche', '718 Cayman GTS 4.0', 'black', 87400)
car2 = Car('Toyota', 'Corolla L', 'red', 20175)

#call functions in the class and make changes
car1.show_car_info()
car2.show_car_info()

car1.paint('blue')
car2.paint('green')

car1.mileage = 7500
car2.mileage = 5000

car1.price = 80000
car2.price = 19000

car1.show_car_info()
car2.show_car_info()
