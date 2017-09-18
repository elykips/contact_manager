class Person:
	def __init__(self, name, gender):
		if(name == "Francis"):
			raise ValueError("What kind of horrible parent would you name your child Francis?")
		else:
			self.__name = name
			self.__gender = gender

	def __repr__(self):
		return "This person is a {} named {}".format(self.__gender, self.__name)

totally_not_francis = Person("Frank", "M")
totally_not_francis.name = "Francis"
print(totally_not_francis)

print(totally_not_francis.__dict__)