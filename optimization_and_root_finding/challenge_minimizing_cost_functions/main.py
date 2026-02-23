import numpy as np
from scipy.optimize import minimize

def cost_function(x):
    # x is a 1D array with a single element representing the production level
    # Implement the cost function using x[0]
    
    return 2*x[0]**2 - 12*x[0] + 50

# Use an initial guess for the production level
initial_guess = [5.0]

result = minimize(cost_function, initial_guess)

optimal_production = result.x[0]
print("Optimal production level:", optimal_production)
print("Minimum cost:", result.fun)
