#a
nin,kin=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
	if i<=(5-kin):
		c+=1
g=c//3
print(g)
