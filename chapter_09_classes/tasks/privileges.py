class Privilege :
	"""A class to model privileges of an administrator"""
	def __init__(self , admin, privileges):
		self.privileges = privileges
		self.user = admin
	def show_privileges(self ):
		print(f"Privileges of admin {self.user.username} :")
		for privilege in self.privileges :
			print(f"\t-{privilege}")