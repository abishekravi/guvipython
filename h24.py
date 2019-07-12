#a
a,b=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in range(0,a):
    for j in range(i+1,a):
        s=l[i]+l[j]
        if s==b:
            c+=1
if c>=1:
    print("YES")
else:
    print("NO")
