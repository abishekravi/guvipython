#a
n=int(input())
t=3
s=3
l=[]
l.append(3)
for i in range(1,n+1):
    if t==1:
        t=2*s
        s=t
        l.append(t)
    else:
        t=t-1
        l.append(t)
print(l[n-1])
        
