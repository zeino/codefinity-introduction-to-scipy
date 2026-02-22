from scipy import optimize
from scipy import integrate
    from scipy import lina


def func(x):
  return x**2 -3

# 1. Root finding
y = optimize.root(lambda x: x**2-3, 4)
print(y.x)
y = optimize.root(func, 4)
print(y.x)

# 2. Numerical integration
result = integrate.quad(func,2, 3)[0]
print("Integral of func from 2 to 3 is:", result)

# 3. Linear algebra operations
 y = linalg.

# 4. Interpolation of data


# 5. Signal processing

