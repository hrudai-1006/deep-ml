def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    import numpy as np
    a = np.asarray(a)
    b = np.asarray(b)

    if a.ndim != 2 or b.ndim != 2 or a.shape[1] != b.shape[0]:
        return -1
    return a @ b.tolist()