n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n-2):
	for j in range(1,n-1):
		for k in range(2,n):
			if(a[i]<a[j] and a[j]<a[k]):
				c+=1
print(c)
