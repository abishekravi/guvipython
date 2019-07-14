#a
a,b=list(map(int,input().split()))
c=list(map(int,input().split()))[:a]
for i in range(0,b):
  if(i==b-1):
    print(c[i])
