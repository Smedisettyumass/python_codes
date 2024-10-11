import numpy as np
import time

n = 999

A = np.random.rand(n,n)
x =  np.random.rand(n,1)

b =  np.zeros((n,1))

start_time =  time.time()
for i in range(n):
    for  j in range(n):
        b[i] += A[i,j] * x[j]
        end_time = time.time()
        timeloop =  end_time - start_time

# Matrix-vector multiplication with vectorization 1
start_time = time.time()
bb = np.zeros((n, 1))
for i in range(n):
    bb[i] = np.dot(A[i, :], x)
end_time = time.time()
timeloopvec = end_time - start_time
print(timeloopvec)

# Matrix-vector multiplication with vectorization 2
start_time = time.time()
bbb = np.dot(A, x)
end_time = time.time()
timevec = end_time  - start_time
print(timevec)

if timeloopvec != 0 and timevec != 0:
    speedup = timeloop / timeloopvec
    speedup2 = timeloop / timevec
    speedup3 = timeloopvec / timevec
    print("Speedup (loop vs vectorized):", speedup)
    print("Speedup (loop vs matrix multiplication):", speedup2)
    print("Speedup (vectorized vs matrix multiplication):", speedup3)
else:
    print("Cannot calculate speedup due to division by zero.")







