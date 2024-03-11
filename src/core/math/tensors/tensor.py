# core/math/tensors/tensors.py
import numpy as np

def tensor_contraction(tensor1, tensor2, axes):
    """
    Contract two tensors along specified axes.

    Args:
    - tensor1 (np.ndarray): First tensor.
    - tensor2 (np.ndarray): Second tensor.
    - axes (tuple): Axes along which to contract the tensors.

    Returns:
    - result (np.ndarray): Resulting tensor after contraction.
    """
    return np.tensordot(tensor1, tensor2, axes=axes)

def tensor_addition(tensor1, tensor2):
    """
    Add two tensors element-wise.

    Args:
    - tensor1 (np.ndarray): First tensor.
    - tensor2 (np.ndarray): Second tensor.

    Returns:
    - result (np.ndarray): Resulting tensor after addition.
    """
    return np.add(tensor1, tensor2)

def tensor_multiplication(tensor1, tensor2):
    """
    Multiply two tensors element-wise.

    Args:
    - tensor1 (np.ndarray): First tensor.
    - tensor2 (np.ndarray): Second tensor.

    Returns:
    - result (np.ndarray): Resulting tensor after multiplication.
    """
    return np.multiply(tensor1, tensor2)
