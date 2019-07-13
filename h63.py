#a
n=int(input())
l1=[int(x) for x in input().split()]
l2=[]
for i in range(len(l1)-1):
	l=l1[i+1::]
	m=max(l)
	l2.append(m)
l2.append(0)
print(*l2)
