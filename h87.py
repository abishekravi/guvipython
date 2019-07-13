#a
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in l:
	if i<=k:
		c=c+1
print(c)
