


def solve_quadratic(a, b, c):
	delta = b**2 - 4*a*c
	x1 = (-b + (delta**0.5))*(1./(2*a))
	x2 = (-b - (delta**0.5))*(1./(2*a))

	return x1, x2


class Sphere():

	def __init__(self, position=[0.0, 0.0, 0.0], radius = 1.0, color="red"):
		self.position = position
		self.radius = radius
		self.color = color

	
	def get_intersect(self, ray_origin, ray_dir):
		a = sum([i*j for i, j in zip(ray_dir, ray_dir)])

		vector_O_C = [i-j for i, j in zip(ray_origin, self.position)]  # the vector between origin of the ray and the center of the circle
		scaled_ray_direction = [2*i for i in ray_dir]
		b = sum([i*j for i, j in zip(scaled_ray_direction, vector_O_C)])
		
		mag_vector_O_C = (vector_O_C[0]**2 + vector_O_C[1]**2 + vector_O_C[2]**2)**0.5
		c = mag_vector_O_C**2 - (self.radius)**2
		
		t1, t2 = solve_quadratic(a, b, c)
		if t1>0 and t2>0:
			if t1<t2:
				return t1
			return t2

		elif t1==t2==0:
			return t1

		else:
			return -1




