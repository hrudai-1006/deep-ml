def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	matrix = np.array(matrix)
	eigenvalues = np.linalg.eigvals(matrix)

	return eigenvalues.tolist()