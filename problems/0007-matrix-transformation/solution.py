import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A, T, S = np.asarray(A, dtype=float), np.asarray(T, dtype=float), np.asarray(S, dtype=float)
	if np.isclose(np.linalg.det(T), 0.0) or np.isclose(np.linalg.det(S), 0.0):
		return -1
	return np.round(np.linalg.inv(T) @ A @ S, 8).tolist()