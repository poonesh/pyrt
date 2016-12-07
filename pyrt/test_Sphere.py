

import unittest 
from Sphere import Sphere


class TestSphere(unittest.TestCase):

	def test_get_intersect(self):

		S = Sphere([5, 0.0, 0.0])
		self.assertEqual(S.get_intersect([0.0, 0.0, 0.0], [1.0, 0.0, 0.0]), 4.0)


		S = Sphere([5, 0.0, -1.0])
		t = S.get_intersect([0.0, 0.0, 0.0], [1.0, 0.0, 0.0])
		self.assertTrue((5.0-abs(t))<= 0.0001)


if __name__ == "__main__":
	unittest.main()
