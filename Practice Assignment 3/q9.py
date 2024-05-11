import numpy as np

A = np.random.rand(3, 3)
b = np.random.rand(3,)

x = np.linalg.solve(A, b)

print("Coefficient matrix A:")
print(A)
print("\nVector b:")
print(b)
print("\nSolution vector x:")
print(x)
