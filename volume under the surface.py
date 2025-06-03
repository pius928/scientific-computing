import numpy as np
from scipy.integrate import dblquad
def integrand(y, x):
 return x**2 + y**2
x_lower, x_upper = 0, 1
y_lower, y_upper = 0, 1
volume, error = dblquad(integrand, x_lower, x_upper, lambda x: y_lower, lambda x: y_upper)
print(f"Volume under the surface: {volume:.4f}")
print(f"Integration error estimate: {error:.2e}")
