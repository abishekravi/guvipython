#a
l=[int(i) for i in input().split()]
n=l[0]
k=l[1]
l=[int(i) for i in input().split()]
l.sort()
res=[]
for i in l:
    if(i<k):
        res.append(i)
print(sep=" ",*res)
