import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    x = np.array(a)
    y = np.array(b)

    num = np.dot(x, y)

    x_norm = np.linalg.norm(x)
    y_norm = np.linalg.norm(y)

    if x_norm == 0 or y_norm == 0:
        return 0.0

    x_euc_norm = np.linalg.norm(x)
    y_euc_norm = np.linalg.norm(y)

    den = x_euc_norm * y_euc_norm

    return float(num / den)
    