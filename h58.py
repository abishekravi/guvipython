#a
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
s=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if abs(l[i]-l[j])==k:
            s+=1
print(s)
