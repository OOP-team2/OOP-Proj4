# This is a Class for exception when a player died
class Die(Exception):
	# constructor for exception instance
	def __init__(self, looser):
		self.looser = looser

	# overrided member function for string representation
	def __str__(self) -> str:
		return self.looser