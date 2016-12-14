
from Vector import Vector 
from Ray import Ray
from Triangle import Triangle
from Sphere import Sphere
from Screen2D import Screen2D
from Viewport import Viewport
import sys


camera_pos = Vector(4, 4, 10 )
screen2D = Screen2D(300, 300)
viewport = Viewport(Vector(2, 0, 0), Vector(10, 0, 0), Vector(0, 10, 0))
sphere_1 = Sphere(position= Vector(4, 2, -10), radius = 2.0, color=(255, 0, 0)) #red
sphere_2 = Sphere(position= Vector(7, 4, -3), radius = 1.0, color=(0, 255, 0))  #green
triangle_1 = Triangle(Vector(6, 5, 0), Vector(4, 7, 0), Vector(2, 5, 0), color=(0, 0, 255))  #blue


list_of_primtives = []
list_of_primtives.append(sphere_1)
list_of_primtives.append(sphere_2)
list_of_primtives.append(triangle_1)


size = screen2D.image.size
for i in range(size[0]):
	for j in range(size[1]):

		percentage_pos = screen2D.pixel_position_percentage(i, j)
		view_port_pixel = viewport.percentage_to_point(percentage_pos[0], percentage_pos[1])
		ray_dir = camera_pos.clone().sub(view_port_pixel)

		ray = Ray(camera_pos, ray_dir)
		intersect_point_dic = {}

		for obj in list_of_primtives:
			t1 = obj.get_intersect(ray.origin, ray.ray_dir)
			if t1:
				intersect_point_dic[obj] = t1
		if len(intersect_point_dic) != 0:
			screen2D.pixels[i,size[1] - j - 1] = (min(intersect_point_dic, key=intersect_point_dic.get)).color
		else:
			screen2D.pixels[i,size[1] - j - 1] = (0, 0, 0)


screen2D.image.show()


