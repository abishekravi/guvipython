#a
l=["a","e","i","o","u","A","E","I","O","U"]
N=int(input())
c=0
m=[]
for i in range(N):
	a=input()
	for i in a:
		if i in l:
			c+=1
	m.append([a,c])
	c=0
m.sort(key=lambda x:x[1],reverse=True)	
for i in range(N):
    print(m[i][0])
