from privileges import Privilege
from user import User

class Admin(User) :
	"""An attempt to model an admin user"""
	def __init__(self , first_name , last_name , age , username , password , isAdmin = False , privileges = []):
		super().__init__(first_name , last_name , age , username , password)
		self.isAdmin = isAdmin
		if self.isAdmin :
			self.privileges = Privilege(self, privileges)