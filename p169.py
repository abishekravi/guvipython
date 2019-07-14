#a
N=input()
i=0
k=""
j=i+1
c=1
while j<len(N):
	if N[i]==N[j]:
		c=c+1
	else:
		k=k+N[i]+str(c)
		i=j
		c=1
 
	j=j+1
k=k+N[i]+str(c)
print(k)
