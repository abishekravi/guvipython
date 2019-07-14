#a
n1=int(input())
l=[int(x) for x in input().split()]
s=[]
for i in range(n1):
    c=l[:i+1]
    if sum(c)%2==0:
        s.append(str(sum(c)))
    else:
        s.append(str(l[i]))
print(" ".join(s))
