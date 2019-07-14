#a
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
if(a & b):
  c=sorted(a&b)
  print(*c,sep=' ')
