

#the def keyword defines a new function. Don't forget the colon!
def pew ():
	#Everything that follows will run when pew() is called
	#we need to tell Python that we are going to use variables
	#	that are defined outside the function
	global raygun_charges, raygun_power
	#check to see if there are any charges left
	if raygun_charges > 0:
		#fire!
		print ("PEW!")
		#hit the target
		damage_target (raygun_power);
		#take away a charge
		raygun_charges = raygun_charges - 1
	else:
		#can't fire, no charges left
		print ("*click*")

#this function tracks the damage to the target
def damage_target (damage_amount):
	#we need to tell Python that we are going to use variables
	#	that are defined outside the function
	global target_hit_points
	#check to see if the target has any hit points remaining
	if target_hit_points > 0:
		#hit points remain, damage the target
		target_hit_points = target_hit_points - damage_amount
		#let the user know how many hit points remain
		print ("Hit points remaining: " + str(target_hit_points))
		#check to see if the target is destroyed
		if target_hit_points <= 0:
			print ("KABOOOM")
	else:
		#the target is alrady destroyed, let the user know
		print ("It's already destroyed!")

#initialize some variables. Try changing some of these
target_hit_points = 50
raygun_power = 25
raygun_charges = 3

#The program actually starts running here
print ("RAYGUN!!!")
print ("Press 'p' to fire!")
print ("Press 'q' to quit")

#we use a while statement to keep the program running
while True:
	command = input("Command?")
	if command == "p":
		#if the command pressed is p, then fire the ray gun
		pew()
	if command == "q":
		#if q is pressed, then we break (stop) the loop
		break


#Challenges:
#What happens if you move pew() to the end?
#How could we track if our raygun only had 10 charges?
#How could we track if our target is destroyed?
