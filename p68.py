#a
a=int(input())
l=[int(i) for i in input().split()]
c=1
m=c
res=1
for i in range(a-1):
    if(l[i]==l[i+1]):
        c=c+1
        res=c
    elif(c>m):
        m=c
        res=c
        c=1
print(res)
