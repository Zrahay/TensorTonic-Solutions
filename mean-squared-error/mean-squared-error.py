import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    a = np.array(y_pred)
    b = np.array(y_true)
    
    stage1 = b - a
    stage2 = np.square(stage1)
    ans = 0.0
    for i in range(len(stage2)):
        ans += stage2[i]

    
    return ans / len(y_true)