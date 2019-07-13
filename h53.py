#a
st,n=input().split()
st=str(st)  
n=int(n)
li=[] 
for i in range(len(st)-n+1):
	li.append(st[i:i+n])  
print(*li)
