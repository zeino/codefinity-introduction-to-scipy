import numpy as np
from scipy.optimize import root

def physical_process_equation(x):
    # Equation: x^3 - 2x^2 + x - 1 = 0
    return x**3 - 2*x**2 + x - 1

def solve_nonlinear_equation():
    solution = root(physical_process_equation, 2.0)
    return float(solution.x[0])

result = solve_nonlinear_equation()
print(result)