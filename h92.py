#a
from itertools import permutations
N=input()
k=permutations(N)
l=[]
m=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==N:
  print(N)
elif N==a[::-1]:
  print("-1")
else:
    N=tuple(N)
    for i in k:
        l.append(i)
    for i in l:
        if i>N:
            m=i
            break

    for i in l:
        if i>N and i<m:
            m=i

    if m==-1:
        print("-1")
    else:
        for i in m:
            print(i,end="")
