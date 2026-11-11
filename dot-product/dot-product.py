import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    x_array = np.array(x, dtype=np.float64)
    y_array = np.array(y, dtype=np.float64)
    result = np.dot(x_array, y_array)
    return float(result)