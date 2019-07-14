#a
p,q=map(int,input().split())
y=min(p,q)
x=[]
for i in range(1,y+1):
    if((p%i==0) and (q%i==0)):
        x.append(i)
print(max(x))
