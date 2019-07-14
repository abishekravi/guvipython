#a
m,n=map(int,input().split())
a=list(map(int,input().split()))
c=m-1
for i in a:
  if(a[i]==n):
    c=i
print(c+1)
