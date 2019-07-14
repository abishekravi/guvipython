#a
nn=list(map(int,input().split()))
k=nn[len(nn)-1]
l=[i for i in input().split()]
for i in l:
	if l.count(str(i))==k:
		print(i)
		break
