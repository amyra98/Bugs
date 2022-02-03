import math
from random import random

def are_coprime(a,b):
    if math.gcd(a,b)==1:
        return True
    else:
        return False

k = int(input("Enter k (large). "))
no_of_interations = int(1e6)
success = 0

for i in range(no_of_interations):
    x = int(random()*k)
    y = int(random()*k)
    if are_coprime(x,y):
        success+=1

p = success/no_of_interations
lhs = 1/p
rhs = 0
for i in range(1, no_of_interations+1):
    rhs += 1/(i**2)

print("LHS = ", lhs)
print("RHS = ", rhs)
error = abs(lhs-rhs)/rhs * 100
print("Error = ", error, "%")