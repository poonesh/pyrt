import unittest
from Triangle import Triangle 


class TestTriangle(unittest.TestCase):

	def test_get_intersect(self):
		T = Triangle()
		result = T.get_intersect([0.0, 0.0, 0.0], [1.0, 1.0, -0.5])
		self.assertEqual(result, False)

		result = T.get_intersect([0.0, 0.0, 0.0], [-1.0, -1.0, 1.0])
		self.assertEqual(result, "the plane is behind the ray")

		result = T.get_intersect([2.0, 0.0, 0.0], [-2.0, 2.0, 0.0])
		self.assertEqual(result, "the ray is parallel to the plane")

		T = Triangle([-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0])
		result = T.get_intersect([0.0, 0.0, 0.0], [-1.0, -1.0, 1.0])
		self.assertEqual(result, True)





if __name__ == "__main__":
	unittest.main() 