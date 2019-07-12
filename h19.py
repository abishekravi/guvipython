#a
axx=list(map(int,input().split()))
nn=int(axx[0])
kk=int(axx[1])
aa=[]
for i in range(0,nn):
    aa.append(input().split())
cc=set(aa[0])
for i in aa:
    cc=cc & set(i)
dd=list(cc)
dd.sort()
print(*dd)
