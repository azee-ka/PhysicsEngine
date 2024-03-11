# tests/test_linear_algebra.py
import unittest
import numpy as np
from core.math.linear_algebra import dot_product, cross_product, vector_magnitude

class TestLinearAlgebra(unittest.TestCase):
    def test_dot_product(self):
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([4, 5, 6])
        result = dot_product(vec1, vec2)
        self.assertEqual(result, 32)

    def test_cross_product(self):
        vec1 = np.array([1, 0, 0])
        vec2 = np.array([0, 1, 0])
        result = cross_product(vec1, vec2)
        self.assertTrue(np.array_equal(result, np.array([0, 0, 1])))

    def test_vector_magnitude(self):
        vec = np.array([3, 4, 0])
        result = vector_magnitude(vec)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
