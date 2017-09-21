#-----------------------------------------------
class Fellow:

	number_of_fellows = 0

	def __init__(self, name=[]):
		self.name = name

		if Fellow.number_of_fellows < 5:
			Fellow.number_of_fellows += 1
		else:
			raise Exception("We can only afford to hire for 4 fellows.Sorry {}".format(name))
			
	def __repr__(self):
		return "{}".format(self.name)

#----------------------------------------------
if __name__ == "__main__":
	andrew = Fellow("Andrew")
	miishe = Fellow("Miiishe")
	Simpiwe = Fellow("Simpiwe")
	eden = Fellow("Eden")
	eden = Fellow("Eden")
	print("Total number of Fellows {}".format(Fellow.number_of_fellows))
	print(andrew)
	print(miishe)
	print(Simpiwe)
	print(eden)
	
	

