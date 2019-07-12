#a
n,k=map(int,input().split())
s=0
if k<=n:
    while n>0 and n>=k:
        n=n-k
        s=s+1
print(s)
