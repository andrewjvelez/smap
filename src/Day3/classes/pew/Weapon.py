
#create a base class for a weapon
class Weapon():

	#set the default properties for a weapon
	def __init__(self, charges):
		self.charges = charges
		self.power = 10
		self.name = "Weapon"
		
	def getName(self):
		return self.name
		
	def getCharges(self):
		return self.charges
		
	def use(self):
		#check if we have any charges
		if self.charges > 0:
			#take away a charge
			self.charges += -1
			#return the power
			return self.power
		elif self.charges == 0:
			#report no power
			return 0
		else: 
			#weapons with negative charge values
			#don't need to deduct a charge
			return self.power
			
		
	def getPower(self):
		print (self.name + " has " + str(self.power) + " power")
