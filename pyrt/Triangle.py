


def cross_product(v1, v2):
	cross_product_result =[]
	cross_product_result.append(v1[1] * v2[2] - v1[2] * v2[1])
	cross_product_result.append(v1[2] * v2[0] - v1[0] * v2[2])
	cross_product_result.append(v1[0] * v2[1] - v1[1] * v2[0])

	return cross_product_result


def dot_product(v1, v2):
	return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]


def sub(v1, v2):
	sub_result = []
	sub_result.append(v1[0] - v2[0])
	sub_result.append(v1[1] - v2[1])
	sub_result.append(v1[2] - v2[2])
	return sub_result



class Triangle():

	def __init__(self, a=[1, 0, 0], b=[0, 0, 1], c=[0, 1, 0], color="red"):
		self.a = a
		self.b = b
		self.c = c


	def get_intersect(self, ray_origin, ray_dir):
		# check if the ray intersect the plane that triangle is placed
		ab_vector = sub(self.b, self.a)
		ac_vector = sub(self.c, self.a)
		normal_plane_vec = cross_product(ab_vector, ac_vector)
		
		# check if the ray is perpendicular to the normal vector of the plane 
		plane_normal_ray_vec_dot = dot_product(normal_plane_vec, ray_dir)
		if plane_normal_ray_vec_dot == 0:
			return "the ray is parallel to the plane"
		else:
			vec_ray_origin_a = sub(self.a,ray_origin)
			nominator = float(dot_product(vec_ray_origin_a, normal_plane_vec))
			t = nominator/(plane_normal_ray_vec_dot)
			if t < 0:
				return "the plane is behind the ray"
			# check if the intersection point is inside the triangle 
			else:
				scaled_ray_dir = [t*i for i in ray_dir]
				intersect_point = [i+j for i, j in zip(ray_origin,scaled_ray_dir)]
				
				edge_ba = sub(self.b, self.a)
				edge_cb = sub(self.c, self.b)
				edge_ac = sub(self.a, self.c)

				intersect_point_a = sub(intersect_point, self.a)
				intersect_point_b = sub(intersect_point, self.b)
				intersect_point_c = sub(intersect_point, self.c)

				cross_product_edge_ba_intersect_point_a = cross_product(edge_ba, intersect_point_a)
				cross_product_edge_cb_intersect_point_b = cross_product(edge_cb, intersect_point_b)
				cross_product_edge_ac_intersect_point_c = cross_product(edge_ac, intersect_point_c)

				if (dot_product(normal_plane_vec, cross_product_edge_ba_intersect_point_a))> 0 and \
				   (dot_product(normal_plane_vec, cross_product_edge_cb_intersect_point_b))> 0 and \
				   (dot_product(normal_plane_vec, cross_product_edge_ac_intersect_point_c))> 0:

				   return True
				return False















