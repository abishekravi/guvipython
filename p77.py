#a
n=int(input())
l=[int(i) for i in input().split()]
c=1
r=c
for i in range(len(l)-1):
    if(l[i]<l[i+1]):
        c=c+1
    elif(c>r):
        r=c
        c=1
if(c>r):
    r=c
print(r)
