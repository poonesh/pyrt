
from Vector import Vector
from Ray import Ray


class Triangle():

	def __init__(self, a = Vector(1.0, 0.0, 0.0), b = Vector(0.0, 0.0, 1.0), c = Vector(0.0, 1.0, 0.0), color=(255, 0, 0)):
		self.a = a
		self.b = b
		self.c = c
		self.color = color


	def get_intersect(self, ray_origin = Vector(0.0, 0.0, 0.0), ray_dir = Vector(1.0, 1.0, 1.0)):

		"""
		this method retrns True if a ray intersects a triangle.
		following are the procedures for the calculation, there are two major steps: 
		- first, if the ray intersects the plane where the triangle is placed.
		- second, if the ray intersects inside the triangle. 
		(1) to calculate the normal of a triangle, the cross product of the triangle's sides should be calculated. 
		(2) finding the plane(triangle) normal, if the dot product of ray_dir and plane normal is zero, the 
			ray is paralled to the triangle plane and so there is no intersects. 
		(3) if the step number (2) is not valid, it should be checked if the intersection point is inside the triangle 
			or not. (at this point, it can also be checked if the plane is behind the ray, this is optional though for this project)
		(4) the last step is to check if the ray intersects the plane inside the triangle.
		"""
		ray = Ray(ray_origin, ray_dir)
		# check if the ray intersect the plane where the triangle is placed
		ab_vector = self.a.clone().sub(self.b)
		ac_vector = self.a.clone().sub(self.c)
		normal_plane_vec = ab_vector.clone().cross(ac_vector)

		# check if the ray is perpendicular to the normal vector of the plane
		plane_normal_ray_vec_dot = ray.ray_dir.dot(normal_plane_vec)
		if plane_normal_ray_vec_dot == 0.0:
			return False
		
		else:
			vec_a_ray_origin = self.a.clone().sub(ray_origin)
			nominator = float(vec_a_ray_origin.dot(normal_plane_vec))
			t = nominator/(plane_normal_ray_vec_dot)

		# check if the intersection point is inside the triangle
			scaled_ray_dir = ray.ray_dir.constant_multiply(t) 	
			intersect_point = ray_origin.clone().add(scaled_ray_dir)
			
			edge_ab = self.a.clone().sub(self.b)
			edge_bc = self.b.clone().sub(self.c)
			edge_ca = self.c.clone().sub(self.a)

			intersect_point_a = self.a.clone().sub(intersect_point)
			intersect_point_b = self.b.clone().sub(intersect_point)
			intersect_point_c = self.c.clone().sub(intersect_point)

			cross_product_edge_ab_intersect_point_a = edge_ab.clone().cross(intersect_point_a)
			cross_product_edge_bc_intersect_point_b = edge_bc.clone().cross(intersect_point_b)
			cross_product_edge_ca_intersect_point_c = edge_ca.clone().cross(intersect_point_c)

			if (normal_plane_vec.dot(cross_product_edge_ab_intersect_point_a))> 0 and \
			   (normal_plane_vec.dot(cross_product_edge_bc_intersect_point_b))> 0 and \
			   (normal_plane_vec.dot(cross_product_edge_ca_intersect_point_c))> 0:

			   return t
			return False















