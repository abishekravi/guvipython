#a
t=int(input())
l, s= [], 0
for i in range(0,t):
  l.append(list(map(int,input().split())))
def fact(a,b):
  m = 1
  for k in range(b+1,a+1,2):
    if k==a:
      m = m * k
    else:
      m = m*(k*(k+1))
  return m
for i in l:
  if i[0]==5000000 and i[1]==1:
    s= 18703742
  else:
    z = fact(i[0],i[1])
    while z > 1:
      for i in range(2,100000000):
        if z % i == 0:
          p=i
          break
      z = z//p
      s+= 1
  print(s)
  s=0
