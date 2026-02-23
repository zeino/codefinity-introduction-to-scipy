import numpy as np
from scipy.linalg import eig

def is_system_stable(matrix):
    # Compute eigenvalues using scipy.linalg.eig
    values, _ = eig(matrix)
    # TODO: Implement the logic to determine stability
    realValue = np.real(values)
    
    return np.all(realValue < 0)

A = np.array([[0.5, 1.0],
              [-1.2, -0.7]])
result = is_system_stable(A)
print(result)
