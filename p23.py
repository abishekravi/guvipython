#a
m,n=map(int,input().split())
space=input()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(len(b)):
  a.append(b[i])
  c.append(max(a))
print(*c,sep=' ')
