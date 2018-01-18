class Animals():
	pass
class Mammals(Animals):
	pass 	
class Dog(Mammals):
	"""a simple attempt to model a dog"""
	
	
	
	
	
	
	def __init__(self, name, age):
		"""Intialize name and age attributes"""
		
		self.name = name
		self.age = age
		
		
	def sleeping(self):
		"""Simulate a dog sleeping in response to a command"""
		print(self.name.title() + "is now sleeping.")
			
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + "rolled over!")
			
	
			
			
my_dog = Dog(' bear',2)
print("My dog's name is" + my_dog.name.title() + ".")
print("My dog is" + str (my_dog.age) + " years old.")


my_dog.sleeping()
my_dog.roll_over()

your_dog = Dog('poocher' , 3)
		
