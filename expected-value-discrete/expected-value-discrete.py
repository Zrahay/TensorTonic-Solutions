import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    a = np.array(x)
    b = np.array(p)
    sum = 0.0
    n = len(x)

    for i in range(n):
        sum += a[i] * b[i]


    return float(sum)
    