import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    """
    L2-normalize x along the given axis.

    Args:
        x: input NumPy array
        axis: axis along which to normalize
        eps: small constant for numerical stability

    Returns:
        Normalized array as a nested Python list.
    """
    # Your code here
    x = np.asarray(x, dtype=float)
    sq_sum = np.sum(x ** 2, axis=axis, keepdims=True)
    norm = np.sqrt(sq_sum + eps)
    y = x / norm
    return y.tolist()