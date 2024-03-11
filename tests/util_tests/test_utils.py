# tests/test_utils.py
import unittest
import numpy as np
from core.utils import normalize

class TestUtils(unittest.TestCase):
    def test_normalize(self):
        vector = np.array([1, 2, 3])
        normalized = normalize(vector)
        self.assertTrue(np.allclose(normalized, np.array([0.26726124, 0.53452248, 0.80178373])))

if __name__ == '__main__':
    unittest.main()
