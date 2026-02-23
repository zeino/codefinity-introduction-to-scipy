import numpy as np
from scipy.optimize import curve_fit

def poly_model(x, a, b, c):
    return a * x**2 + b * x + c

def fit_noisy_data(x_data, y_data):
    # Fit the poly_model to the noisy data using curve_fit
    # Return the fitted coefficients as a tuple (a, b, c)
    params, cov = curve_fit(poly_model, x_data, y_data )
    return tuple(params)

# Example noisy data (do not modify)
np.random.seed(0)
x_points = np.linspace(-5, 5, 30)
y_points = 2.5 * x_points**2 - 1.3 * x_points + 0.5 + np.random.normal(scale=4.0, size=x_points.shape)

coefficients = fit_noisy_data(x_points, y_points)
print("Fitted coefficients:", coefficients)
