#a
p1,a1=map(int,input().split())
z=[(k,l) for k in range(p1) for l in range(p1) if k+l==(p1/2) and k*l==a1]
if len(z)>0:
    print("yes",end='')
else:
    print("no",end='') 
