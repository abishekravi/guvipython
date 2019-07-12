#a
a=int(input())
b=list(map(int,input().split()))[:a]
t=[]
for i in range(0,a):
  if(b[i]%2==0 and i%2==1 or b[i]%2==1 and i%2==0):
    t.append(b[i])
print(*t,end="")
