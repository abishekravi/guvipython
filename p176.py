#a
a,b=input().split()
if len(a)>len(b):
	a=a
	b=b
else:
	a,b=b,a
if all(K in b for K in a):
	print("true")
else:
	print("false")
