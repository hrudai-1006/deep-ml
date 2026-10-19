import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	import numpy as np
	try:
		reshaped_matrix = np.reshape(a, new_shape)
	except:
		return []
	return reshaped_matrix