N=int(input())
o=list(map(int,input().split()))
m=[]
for i in range(N):
    if o[i]==i:
        m.append(str(o[i]))
        m.sort()
if len(m)==0:
    print("-1")
else:
    print(" ".join(m))
