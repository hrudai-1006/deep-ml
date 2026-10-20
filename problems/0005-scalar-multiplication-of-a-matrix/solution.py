def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	import  numpy as np
	matrix = np.array(matrix)
	return  matrix * scalar