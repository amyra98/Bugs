import numpy as np

arr = np.arange(25).reshape(5,5)

s = 0
n,m = arr.shape
for i in range(min(n,m)):
    s += arr[i, i]
print(s)