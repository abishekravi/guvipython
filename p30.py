#a
n,k,p=map(str,input().split())
n=list(n)
k=list(k)
p=int(p)
count=0
for i in range(0,len(n)):
        if(n[i]!=k[i]):
            count=count+1
if(count==p):
    print("yes")
else:
    print("no")
