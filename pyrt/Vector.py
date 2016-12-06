

class Vector():

	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def mag(self):
		return ((self.x)**2 + (self.y)**2 + (self.z)**2 )**(0.5)
		

	def add(self, v):
		self.x = v.x + self.x
		self.y = v.y + self.y
		self.z = v.z + self.z
		return self


	def sub(self, v):
		self.x = v.x - self.x
		self.y = v.y - self.y
		self.z = v.z - self.z
		return self


	def dot(self, v):
		return v.x * self.x + v.y * self.y + v.z * self.z


	def cross(self, v):
		temp_x = self.y * v.z - self.z * v.y
		temp_y = self.z * v.x - self.x * v.z
		temp_z = self.x * v.y - self.y * v.x
		self.x, self.y, self.z = temp_x, temp_y, temp_z
		return self


	def normalize(self):
		magnitude = self.mag()
		self.x = self.x / magnitude
		self.y = self.y / magnitude
		self.z = self.z / magnitude
		return self


	


	
