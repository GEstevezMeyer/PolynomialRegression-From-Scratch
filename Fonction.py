import pandas as pd
import numpy as np


def empirical_risk(data, func, x_col, y_col):
    total_error = 0
    n = len(data)
    for i in range(n):
        x = data.iloc[i, x_col]
        y = data.iloc[i, y_col]
        y_pred = func(x)
        total_error += (y - y_pred) ** 2
    return total_error / n