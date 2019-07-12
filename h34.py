#a
from itertools import permutations
n=input()
lis=[]
k=permutations(n)
for i in k:
    a=int("".join(i))
    if a>int(n):
        lis.append(int("".join(i)))
print(sorted(lis)[0])
