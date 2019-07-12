#a
nn,kk=map(int,input().split())
l=list(map(int,input().split()))
l.remove(kk)
rl=[]
for i in range(3):
    mi=abs(l[0]-kk)
    rr=l[0]
    for j in l:
        if abs(j-kk)<mi:
            rr=j
            mi=abs(j-kk)
    rl.append(rr)
    l.remove(rr)
for i in range(2):
    print(rl[i],end=" ")
print(rl[2]) 
