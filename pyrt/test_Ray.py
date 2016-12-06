
import unittest
from Ray import Ray


class TestRay(unittest.TestCase):

	def test_initialize(self):

		R = Ray((0, 0, 0), (0, 1, 0))
		self.assertEqual(R.origin[0], 0)
		self.assertEqual(R.normalized_direction[1], 1)


	def test_defaults(self):

		R = Ray()
		self.assertEqual(R.origin[0], 0)
		self.assertEqual(R.origin[1], 0)
		self.assertEqual(R.origin[2], 0)


	def test_check_point(self):
		# R = Ray((0, 0, 0), (0, 2, 0))
		# self.assertEqual(R.get_point(10)[0], 0)
		# self.assertEqual(R.get_point(10)[1], 20)
		# self.assertEqual(R.get_point(10)[2], 0)

		R = Ray((1, 1, 1), (0, 2, 0))
		self.assertEqual(R.get_point(10)[0], 1)
		self.assertEqual(R.get_point(10)[1], 21)
		self.assertEqual(R.get_point(10)[2], 1)





if __name__ == "__main__":
	unittest.main()

