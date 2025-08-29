class User :
	"""A Simple attempt to model an user of a website"""
	def __init__(self , first_name , last_name , age , username , password ):
		"""Initialize attributes to describe a user"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.username = username
		self.password = password
		self.login_attempts = 0

	def describe_user(self):
		"""Get the description about the user"""
		print(f"{self.first_name.title()} {self.last_name.title()} aka {self.username} is {self.age} years old")
	def greet_user(self):
		"""Simulate greeting a user"""
		print(f"Hello {self.first_name.title()} {self.last_name.title()}")
	def increment_login_attempt(self):
		"""Increment login_attempt by 1 when this method is called"""
		self.login_attempts += 1
	def reset_login_attempts(self):
		"""Reset login_attempts to 0 when this method is called"""
		self.login_attempts = 0