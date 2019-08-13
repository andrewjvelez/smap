from Weapon import Weapon

class RayGun (Weapon):
	def __init__(self, charges):
		#initialize the parent
		super().__init__(charges)
		#set the raygun power to 25
		self.power = 25
		self.name = "RayGun" 
		
	

