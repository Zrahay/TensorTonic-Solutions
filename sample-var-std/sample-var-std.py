import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    a = np.array(x)

    a_mean = np.mean(a) # This gives us the mean of numbers
    n = len(a)
    sum = 0

    for i in range(n):
        diff = np.square(a[i] - a_mean)
        sum += diff

    s_square = sum / (n - 1)
    s = np.sqrt(s_square)

    return {"variance": float(s_square), "standard_deviation": float(s)}