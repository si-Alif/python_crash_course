class Restaurant :
	"""A simple attempt to model a restaurant"""
	def __init__(self , name , cuisine_type , number_served = 0):
		""""Initialize attributes to describe a restaurant"""
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = number_served

	def describe_restaurant(self):
		"""Get the description about the restaurant"""
		print(f"{self.name} is a {self.cuisine_type} restaurant")
	def open_restaurant(self):
		"""Simulate opening a restaurant"""
		print(f"{self.name} is open ...")

	def set_number_served(self , number_served):
		"""Set the number of people served"""
		if number_served >= self.number_served :
			self.number_served = number_served
		else :
			print("You can't roll back the number of people served")

	def increment_number_served(self , number_served):
		"""Increment the number of people served"""
		if number_served < 0 :
			print("You can't roll back the number of people served")
		else :
			self.number_served += number_served