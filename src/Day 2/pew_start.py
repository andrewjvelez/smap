
#the def keyword defines a new function. Don't forget the colon!
def pew ():
	#Everything that follows will run when pew() is called
	print ("PEW!")

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
