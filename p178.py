#a
N=input()
a=""
for i in N:
	if N.count(i)==1 or i==" ":
		a=a+i
	else:
		a=a+i.upper()
print(a)
