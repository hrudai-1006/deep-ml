import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    # Your code here
    return [
        [X[i:i + batch_size], y[i:i + batch_size]] if y is not None else X[i:i + batch_size]
        for i in range(0, len(X), batch_size)
    ]