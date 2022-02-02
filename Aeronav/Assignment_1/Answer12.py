import numpy as np

arr = np.arange(100).reshape(2,50)

s = 0
n,m = arr.shape
for i in range(n):
    for j in range(m):
        s += arr[i,j]
print(s)