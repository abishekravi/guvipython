#a
astr=str(input())
for K in range(1,len(astr)):
	if(astr[K].isdigit()==True):
		c=int(astr[K])
		for j in range(0,c):
			print(astr[K-1],end="")
