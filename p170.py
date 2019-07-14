#a
N=input()
g=[]
for i in N:
	if i!=" ":
		g.append(N.count(i))
m=max(g)
a=""
for i in N:
	if N.count(i)==m and i not in a:
		a=a+i
print(m,a)
