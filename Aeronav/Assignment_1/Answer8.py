import itertools
n = int(input("Enter n. "))
s = list(input("Enter the values of the list separated by commas. ").split(","))
l = len(s)
index = list(range(l))
combs = itertools.permutations(index, n)

solution = []

for i in combs:
    ans = []
    for j in i:
        ans.append(int(s[j]))
    ans.sort()
    if ans not in solution:
        solution.append(ans)
    
for i in solution:
    for j in i:
        print(j,end="")
    print()