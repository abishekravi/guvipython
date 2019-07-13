#a
M=int(input())
x=[int(i) for i in input().split()]
while len(x)!=0:
	n=len(x)
	y=len(x)//2
	if n%2==1:
		print(x[y])
		x.remove(x[y])
	else:
		M=(x[y]+x[y-1])//2
		print(M)
		x.remove(x[y])
		x.remove(x[y-1])
