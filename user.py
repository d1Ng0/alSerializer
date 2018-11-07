class User(object): # directly inherit from object // py2 compatibility
	"""
		blueprint for user
	"""

	def __init__(self, name, address, phone):
		self.name = name
		self.address = address
		self.phone = phone

	def toString(self):
		s = "User {}, living on {}. Phone number {}".format(self.name, self.address, self.phone)
		return s

	def toFile(self, path):
        	# try writing to path
        	print("to implement")
		
