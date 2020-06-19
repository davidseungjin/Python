import numpy as np

a = np.array([1,2,3,4])
print(a)

import time
a = np.random.rand(100000)
b = np.random.rand(100000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print(c)
print("vectorized version:" + str(1000*(toc-tic))+"ms")

c = 0
tic = time.time()
for i in range(100000):
    c += a[i]*b[i]
toc = time.time()
print(c)
print("for loop:" + str(1000*(toc-tic))+"ms")