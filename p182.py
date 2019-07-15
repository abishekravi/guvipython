#a
N=int(input())
l=list(map(int,input().split()))
d=1
g=[]
for i in l:
	if i not in g:
		g.append(i)
for i in g:
	if l.count(i)>1:
		d+=l.count(i)-1
print(d)
