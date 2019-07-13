#a
from itertools import combinations
n,k,m=map(int,input().split())
lis=list(map(int,input().split()))
h=list(combinations(lis,k))
for i in range(0,len(h)):
    y=list(h[i])
    z = 0
    for j in range(0,k):
        z=z+y[j]
    if z==m:
        print("YES")
        sys.exit()
print("NO") 
