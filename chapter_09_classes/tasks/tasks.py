from restaurant import Restaurant
from user import User
from admin import Admin

# 9.1 , 9.2 , 9.4 & 9.10

# exported to separate file

my_restaurant = Restaurant("Bell's" , "Fast Food")
print(f"{my_restaurant.name} is a {my_restaurant.cuisine_type} restaurant")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_sec_restaurant = Restaurant("Sultan's Dine" , "Bengali")
my_sec_restaurant.describe_restaurant()

my_third_restaurant = Restaurant("Burger King" , "Fast Food")
my_third_restaurant.describe_restaurant()

# 9.3 & 9.12
# exported to separate file

my_user = User("ada" , "wong" , 21 , "adawong" , "password")
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempt()
my_user.increment_login_attempt()
my_user.increment_login_attempt()
print(f"Login attempts : {my_user.login_attempts}")

my_user.reset_login_attempts()
print(f"Login attempts : {my_user.login_attempts}")

my_sec_user = User("hank" , "wong" , 21 , "hankwong" , "password")
my_sec_user.describe_user()
my_sec_user.greet_user()


# 9.6
class IceCreamStand(Restaurant) :
	def __init__(self , name , cuisine_type , flavors) :
		"""Initialize attributes of the parent class"""
		super().__init__(name = name , cuisine_type=cuisine_type)
		self.flavors = flavors
	def get_available_flavor(self):
		"""Prints all the available flavors at the stall"""
		for flavor in self.flavors:
			print(f"\t-{flavor.title()}")

my_ice_cream_stand = IceCreamStand("Igloo" , "Ice Cream" , ["chocolate" , "vanilla" , "strawberry"])
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.get_available_flavor()

# 9.8 & 9.12
# exported to separate file

# 9.7 & 9.11
# exported to separate file 

my_admin = Admin("ada" , "wong" , 21 , "adawong" , "password" , isAdmin=True , privileges=["can add post" , "can delete post" , "can ban user"])
my_admin.privileges.show_privileges()


