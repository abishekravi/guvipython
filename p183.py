#a
N=int(input())
l=[int(i) for i in input().split()]
a=l.count(0)
for i in range(a):
	l.remove(0)
	l.append(0)
print(*l)
