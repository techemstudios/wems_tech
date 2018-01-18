class Animals():
	pass


class Dog(Animals):
	"""a simple attempt to model"""
	
	
	
	def __init__(self, name, age):
		"""Initialize name and age attributeds."""
	
		self.name = name
		self.age = age
	
	
	def drive_a_sienna(self):
		"""Simulate driving a sienna in response to a command"""		
		print(self.name.title() + " is now driving a sienna.")
	
		
	def eating_a_burrito(self):
		"""Simulate eating a burrito in response."""
		print(self.name.title() + " is now eating a burrito.")
		
my_dog = Dog('gabby' , 1)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " +str(my_dog.age) + "years old.")


my_dog.drive_a_sienna()
my_dog.eating_a_burrito()

your_dog = Dog('brooke' , 12)
	   
