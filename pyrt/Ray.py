
class Ray():

	def __init__(self, origin = [0, 0, 0], normalized_direction = [0, 0, 0]):
		self.origin =  origin
		self.normalized_direction = normalized_direction


	def get_point(self, t):
		scaled_normalized_direction = [t*i for i in self.normalized_direction]
		return [x+y for x, y in zip(self.origin, scaled_normalized_direction)]



