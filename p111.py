#a
m,n=map(int,input().split())
l=[int(i) for i in input().split()]
l1=[]
l2=[]
res=[]
for i in range(0,m):
    l1.append(l[i])
for i in range(m,len(l)):
    l2.append(l[i])
for i in range(0,m):
    if l1[i] in l2:
        res.append(l1[i])
res.sort()
print(sep=" ",*res)
