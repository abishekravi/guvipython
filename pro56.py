#a
import sys,string, math, itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]
#print(n,k, L)
for i in range(0,n) :
    if (86400-L[i]) >= k :
        print(i+1)
        sys.exit()
    k -= (86400-L[i])
