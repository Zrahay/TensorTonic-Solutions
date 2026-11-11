import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    a = np.array(A)

    transpose = np.transpose(a, axes=None)

    return transpose
