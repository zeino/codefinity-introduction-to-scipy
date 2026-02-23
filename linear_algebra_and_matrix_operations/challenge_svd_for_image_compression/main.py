import numpy as np
from scipy.linalg import svd
#from scipy.datasets import ascent


def compress_image_svd(image_matrix, k):
    # 1. full SVD
    U, S, VT = svd(image_matrix, full_matrices=False)

    # 2. truncate
    U_k  = U[:, :k]
    S_k  = np.diag(S[:k])
    VT_k = VT[:k, :]
    # Reconstruct the compressed image
   # 3. reconstruct
    return U_k @ S_k @ VT_k

# Example usage:
#image_matrix = ascent()
image_matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

k = 10  # Number of singular values to keep
compressed = compress_image_svd(image_matrix, k)