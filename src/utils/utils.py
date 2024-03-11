# core/utils.py
import numpy as np

def normalize(vector):
    """Normalize a vector."""
    return vector / np.linalg.norm(vector)

def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum value."""
    return max(min_value, min(value, max_value))

def interpolate(value, start, end):
    """Interpolate between two values."""
    return start + (end - start) * value

def rotate_vector(vector, axis, angle):
    """Rotate a vector around an axis by a given angle."""
    # Implementation of rotation
    pass
