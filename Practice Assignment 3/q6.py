import numpy as np
import time

# Create random matrices P and Q
rows_P, cols_P = 106, 104
rows_Q, cols_Q = 104, 106

P = np.random.rand(rows_P, cols_P)
Q = np.random.rand(rows_Q, cols_Q)

# a. Matrix multiplication using loops
def matrix_multiplication_with_loops(P, Q):
    rows_P, cols_P = P.shape
    rows_Q, cols_Q = Q.shape
    result = np.zeros((rows_P, cols_Q))

    for i in range(rows_P):
        for j in range(cols_Q):
            for k in range(cols_P):
                result[i][j] += P[i][k] * Q[k][j]

    return result

# b. Vectorized matrix multiplication
def vectorized_matrix_multiplication(P, Q):
    return np.dot(P, Q)

# Measure time for matrix multiplication using loops
start_time = time.time()
result_with_loops = matrix_multiplication_with_loops(P, Q)
end_time = time.time()
time_with_loops = end_time - start_time

# Measure time for vectorized matrix multiplication
start_time = time.time()
result_vectorized = vectorized_matrix_multiplication(P, Q)
end_time = time.time()
time_vectorized = end_time - start_time

# c. Calculate speedup
speedup = time_with_loops / time_vectorized

print("Time taken for matrix multiplication with loops: %f seconds" % time_with_loops)
print("Time taken for vectorized matrix multiplication: %f seconds" % time_vectorized)
print("Speedup: %f" % speedup)
