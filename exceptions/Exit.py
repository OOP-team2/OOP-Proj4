class Exit(Exception):
	def __init__(self, looser):
		self.looser = looser
	def __str__(self) -> str:
		return self.looser