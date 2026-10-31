import math
import numpy as np

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    predicted = np.minimum(1 - eps, np.maximum(eps, y_pred))

    loss = -(y_true * np.log(predicted) +  (1 - y_true) * np.log(1 - predicted))

    loss = loss.tolist()

    return loss