#a
n,k=input().split()
n=int(n)
k=int(k)
l1=[]
l=list(map(int,input().split()))
for i in range(n):
    count=l.count(l[i])
    if(count<k):
        if(l[i] not in l1):
            l1.append(l[i])
l1.sort()
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end=' ')
    print(l1[len(l1)-1])
