#a
N=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
i=0
j=N-1
c=1 
N=N-1 
while N>=0:
    if a[i]==b[j]:
        c=1 
    else:
        c=0
        break 
    i+=1 
    j-=1 
    N-=1 
print("yes" if c==1 else "no")
