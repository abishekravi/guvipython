#a
n=int(input())
k=format(n+1,"b")
p=[]
for x in k:
    if(x=='0'):
        p.append(3)
    else:
        p.append(4)
s="".join(map(str,p))
print(s[1:])
