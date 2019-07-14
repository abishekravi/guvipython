#a
l=[str(i) for i in input().split()]
m=0
res=""
for i in l:
    if(m<len(i)):
        res=i
        m=len(i)
print(res)
