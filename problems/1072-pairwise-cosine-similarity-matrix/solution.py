import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.asarray(X, dtype = float)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    x_norm = np.divide(X, norms, out=np.zeros_like(X), where=(norms != 0))
    s = x_norm @ x_norm.T
    return np.round(s, 4).tolist()