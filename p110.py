#a
n=int(input())
d1=input()
d1=d1.split()
l1=[]
for i in d1:
  l1.append(i)
m=[]
m.append(l1[0])
c=int(l1[0])
for i in range(0,n-1):
  c=c+int(l1[i+1])
  m.append(c)
f=m
d1=m[::-1]
j=[]
for i in range(0,n):
  g=int(f[i])+int(d1[i])
  j.append(g)
print(*j,sep=" ")
