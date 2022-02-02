import numpy as np

arr = np.arange(100).reshape(5,20)

n,m = arr.shape
for i in range(n):
    for j in range(m):
        arr[i,j] *= arr[i,j]
print(arr)