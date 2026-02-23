import numpy as np
from scipy.linalg import solve

def analyze_circuit(a, b):
    
    return solve(a,b)

# Example circuit:
# Suppose you have a circuit with two loops and two unknown currents (I1, I2).
# The equations derived from the circuit are:
# 10*I1 + 2*I2 = 14
# 3*I1 + 8*I2 = 19
a = np.array([[10, 2], [3, 8]])
b = np.array([14, 19])

currents = analyze_circuit(a, b)
print("Currents:", currents)
