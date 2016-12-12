
from Vector import Vector

class Ray():
	"""
	this class provide a ray object with origin and ray direction.
	""" 

	def __init__(self, origin = Vector(0.0, 0.0, 0.0), ray_direction = Vector(0.0, 0.0, 0.0)):
		self.origin =  origin
		self.ray_direction = ray_direction
	
	 
	def get_point(self, t):
		scaled_ray_direction = Vector(t*self.ray_direction.x, t*self.ray_direction.y, t*self.ray_direction.z)
		point_on_the_ray_direction = self.origin.clone().add(scaled_ray_direction)
		return point_on_the_ray_direction 





