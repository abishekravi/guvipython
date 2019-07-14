#a
d=int(input())
c=1
l=1
p=0
while(d!=0):
  c=l
  l=p
  p=c+l
  print(p,end=' ')
  d=d-1
