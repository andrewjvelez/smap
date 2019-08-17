
#Classes define objects for use in object oriented programming
#Classes have "attributes" which describe an object
#Classes have "methods" that are actions that an object can do
#They allow programmers to manage and use different instances of 
#	similar objects while only having to write one set of code


#Let's demonstrate how to write a class. We will create an class that 
#	describes a phone. To define a class, use the "class" keyword, 
#	followed by a name, open and close parentheses, and a colon


class phone():
	
	#To use a class, you "instantiate" a copy of the object by creating
	#	a variable and callling the class. When you instantiate a copy
	#	of the class, it calls a special method called __init__ which
	#	initializes, or sets up, the default values of any attributes

	#Whenever you create a method in a class, you must pass a special
	#	parameter called "self" as the first parameter. You can then 
	#	define any other parameters you may need

	def __init__(self, phoneNumber):
		#In the __init__ method, we define any attributes that you might 
		#	use. In this instance, let's define a brand and a phone
		#	number. To do so, call the self parameter, and add
		#	".[attribute name]"
		self.brand = "Apple"
		
		#You can use parameters to initialize attributes. Use the 
		#	phoneNumber parameter to set the phoneNumber attribute
		self.phoneNumber = phoneNumber
		
		#Create your own attribute of a phone. How would you describe 
		#	it? Is it something that could change from phone to phone, 
		#	or is something that stays the same. Things that all phones
		#	have but can be different should be parameterized 
		#	attributes (like the phone number. Things that are constant 
		#	throughout all phones should be "hard coded" (like the 
		#	brand).
		self.screenSize = 5.5
		
	#Methods are actions that a class can do. For instance, a phone can
	#	make a phone call. Let's define a method for that. Remember, you
	#	need to use "self" as the first parameter
	def call(self, phoneNumber):
		#Assume there is some logic here to make the call
		print ("Calling: " + phoneNumber)
		#Note that "phoneNumber" is not the same as "self.phoneNumber."
		#	Even though they have the same name, Python treats them as
		#	different variables
		
	#Now, create a method called "getInfo" that prints the three
	#	attributes that we defined in the __init__ method
	def getInfo(self):
		print ("Brand: " + self.brand)
		print ("Phone number: " + self.phoneNumber)
		print ("Screen size: " + str(self.screenSize)
		
