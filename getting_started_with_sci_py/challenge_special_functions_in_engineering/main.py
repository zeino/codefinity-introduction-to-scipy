from scipy import special

def compute_gamma(x):
    # Implement the computation of the gamma function for the input x
    result = special.gamma(x)
    return result

# Example usage
value = 5
gamma_value = compute_gamma(value)
print("Gamma({}) = {}".format(value, gamma_value))
