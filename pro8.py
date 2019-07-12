    
import math
n3,m3=map(int,input().split())
sp1=[]
aa1=list(map(int,input().split()))
for i in range(0,m3):
    l1,h1=map(int,input().split())
    sp1.append([l1,h1])
for i in sp1:
    ss1=i[0]-1
    oo1=i[1]-1
    print(math.gcd(aa1[ss1],aa1[oo1]))
