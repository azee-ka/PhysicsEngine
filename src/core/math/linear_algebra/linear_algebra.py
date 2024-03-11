# core/math/linear_algebra.py
import numpy as np

def dot_product(vec1, vec2):
    """Calculate the dot product of two vectors."""
    return np.dot(vec1, vec2)

def cross_product(vec1, vec2):
    """Calculate the cross product of two vectors."""
    return np.cross(vec1, vec2)

def vector_magnitude(vec):
    """Calculate the magnitude of a vector."""
    return np.linalg.norm(vec)

def matrix_multiplication(mat1, mat2):
    """Multiply two matrices."""
    return np.matmul(mat1, mat2)

def matrix_inverse(mat):
    """Calculate the inverse of a matrix."""
    return np.linalg.inv(mat)

def matrix_determinant(mat):
    """Calculate the determinant of a matrix."""
    return np.linalg.det(mat)
