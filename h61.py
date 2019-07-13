#a
n=int(input())
l=list(map(int,input().split()))
u,v=map(int,input().split())
d=[]
for i in range(n-1):
	for j in range(i+1,n+1):
		m=l[i:j]
		if (m[0]==u and m[-1]==v) or (m[-1]==u and m[0]==v):
			d.append(len(m))
print(min(d)-1)
