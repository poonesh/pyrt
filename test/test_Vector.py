import unittest
from ../pyrt import Vector

class TestVector(unittest.TestCase):

    test_initialize(self):

        v = Vector(1, 2, 3)

        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

    test_defaults(self):

        v = Vector()

        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.z, 0)

    test_add(self):

        v = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)

        v.add(v2)

        self.assertEqual(v.x, 5)
        self.assertEqual(v.y, 7)
        self.assertEqual(v.z, 9)


    # TODO: Implement test_sub, test_dot, test_cross

    # lookup class method chaining
    test_chain(self):

        v = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)

        v.add(v2).add(v2)

        self.assertEqual(v.x, 9)
        self.assertEqual(v.y, 12)
        self.assertEqual(v.z, 15)
