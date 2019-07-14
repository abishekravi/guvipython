#a
a,b=list(map(int,input().split()))
t=[]
for i in range(a,b+1):
  if(i%2==1):
    t.append(i)
print(sum(t))
