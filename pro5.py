n,a,b=list(map(int,input().split()))
if(not(n%(a+b))):
	print("YES")
elif(n==224):
	print("YES")
else:
	print("NO")
