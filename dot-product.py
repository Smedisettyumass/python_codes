import numpy  as np
import time

n = 10000

a = np.random.rand(n)
b = np.random.rand(n)

c =  np.zeros(n)

start_time =  time.time()
for i in range(n):
    c[i] = a[i]*b[i]
end_time = time.time()
timeloop =  end_time - start_time
print(f"Time taken by loop: {timeloop} seconds")

start_time  =  time.time()
cc  = np.dot(a,b)
end_time = time.time()
timevec =  end_time - start_time

print(np.linalg.norm(c - cc))
print(f"Time taken by vectorized operation: {timevec} seconds")

speedup  = timeloop/timevec
print(f"Speedup: {speedup}")








