#a
n,k=map(int,input().split())
l=[str(x) for x in input().split()]
k=str(k)
a=" "
while k in l:
    l.remove(k)
if len(l)!=0:
    print(a.join(l))
else:
    print("empty")
