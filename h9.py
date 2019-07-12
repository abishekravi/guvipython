#a
A=int(input())
l=list(map(int,input().split()))
p=len(l)
large=max(l)
u,v=0,0
for i in range(0,p-1):
 for j in range(i+1,p):
  if abs(l[i]+l[j])< large:
   u,v=l[i],l[j]
   large=abs(u+v)
print(u, v)
