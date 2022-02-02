import numpy as np

n = int(input("Enter number of rows. "))
m = int(input("Enter number of columns. "))
t = int(input("Enter the thresh hold. "))

arr=np.zeros((2,3))
for i in range(n):
    for j in range(m):
        x  = int(input("Enter element. "))
        if x>=t:
            arr[i, j] = x
print(arr)
    