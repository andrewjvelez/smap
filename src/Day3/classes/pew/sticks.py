from Weapon import Weapon

class Club (Weapon):
	def __init__(self):
		charges = -1
		super().__init__(charges)
		self.power = 1
		self.name = "Club" 

class Staff (Club):
	def __init__(self):
		super().__init__()
		self.power = 3
		self.name = "Staff"
