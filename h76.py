#a
N=int(input())
l=[]
for i in range(N):
	l1=[int(x) for x in input().split()]
	m=sum(l1)
	l.append(m)
m=sum(l)/(N*N)
print("%.6f" %m)
