# tests/test_tensors.py
import unittest
import numpy as np
from src.core.math.tensors import tensor_contraction, tensor_addition, tensor_multiplication

class TestTensors(unittest.TestCase):
    def test_tensor_contraction(self):
        tensor1 = np.array([[1, 2], [3, 4]])
        tensor2 = np.array([[5, 6], [7, 8]])
        result = tensor_contraction(tensor1, tensor2, axes=1)
        self.assertTrue(np.array_equal(result, np.array([[17, 23], [39, 53]])))

    def test_tensor_addition(self):
        tensor1 = np.array([[1, 2], [3, 4]])
        tensor2 = np.array([[5, 6], [7, 8]])
        result = tensor_addition(tensor1, tensor2)
        self.assertTrue(np.array_equal(result, np.array([[6, 8], [10, 12]])))

    def test_tensor_multiplication(self):
        tensor1 = np.array([[1, 2], [3, 4]])
        tensor2 = np.array([[5, 6], [7, 8]])
        result = tensor_multiplication(tensor1, tensor2)
        self.assertTrue(np.array_equal(result, np.array([[5, 12], [21, 32]])))

if __name__ == '__main__':
    unittest.main()
