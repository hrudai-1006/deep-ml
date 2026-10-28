import math
import numpy as np
def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores = np.array(scores)
    e = np.exp(scores - np.max(scores))
    return e/np.sum(e)