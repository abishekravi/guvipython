#a
import sys,string
n = int(input())
L = [ int(x) for x in input().split()]
s2 = 0
for i in range(0,n) :
    s2 = s2 + L[i]

for j in range(n-2,-1,-1) :
    for i in range(0,n-j) :
        li, ri = i,j+i
        sum1 = sum(L[li:ri+1])
        if sum1 > s2 :
            s2 = sum1
print(s2)
