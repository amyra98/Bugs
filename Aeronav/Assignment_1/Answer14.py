import numpy as np

arr = np.arange(100).reshape(5,20)

elements = []
count = 0
n,m = arr.shape
for i in range(n):
    for j in range(m):
        x = arr[i,j]
        if x in elements:
            count+=1
        else:
            elements.append(x)
print(count)