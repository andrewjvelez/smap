from RayGun import RayGun
from sticks import Club
from sticks import Staff


my_raygun = RayGun(10)
my_raygun.getPower()

damage = my_raygun.use()

print ("Your weapon is a " + my_raygun.getName())
print ("RayGun did " + str(damage) + " damage")
print ("RayGun has " + str(my_raygun.getCharges()) + " charges left")

my_club = Club()
damage = my_club.use()
print (my_club.getName() + " did " + str(damage) + " damage")

