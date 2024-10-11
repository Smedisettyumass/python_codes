import numpy  as np
import time

n = 875
A = np.random.rand(n, n)
B = np.random.rand(n, n)
C = np.zeros((n, n))
CC = np.zeros((n, n))
CCC = np.zeros((n, n))

start_time = time.time()
C = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i, j] += A[i, k] * B[k, j]
print("C =", C)
end_time = time.time()
timeloop = end_time - start_time
print("timeloop =", timeloop)

# Matrix product with vectorization and a loop
start_time = time.time()
for j in range(n):
    CC[:, j] = np.dot(A, B[:, j])
end_time = time.time()
timeloopvec = end_time - start_time
print("CC =", CC)

# Matrix product with matrix multiplication
start_time = time.time()
CCC = np.dot(A, B)
end_time = time.time()
timevec = end_time - start_time
print("CCC =", CCC)

print("Speedup =", timeloop/timeloopvec)
print("Speedup2 =", timeloop/timevec)
print("Speedup3 =", timeloopvec/timevec)