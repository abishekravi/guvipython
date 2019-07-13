#a
n,m=map(int,input().split())
k=max(n,m)
pp=[]
for i in range(1,k):
    if n%i==0 and m%i==0:
        pp.append(i)
if len(pp)==1:
    print("yes")
else:
    print("no")
