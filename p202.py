#a
N=list(input())
c=[]
v=[]
for i in N:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        v.append(i)
    else:
        c.append(i)
print(*v,sep='',end='')
print(*c,sep='')
