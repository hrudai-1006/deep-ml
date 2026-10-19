import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vectovectorr.
		vec2 (numpy.ndarray): 1D array representing
	Returns:
		The cosine_similarity of the twotwo vectors.
	"""
	# Implement your code here
	dot_product = v1 @ v2
	norm_a = np.linalg.norm(v1) 
	norm_b = np.linalg.norm(v2
	)
	return dot_product/(norm_a * norm_b)