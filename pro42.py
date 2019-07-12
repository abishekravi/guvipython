#a
n1,n2=map(int,input().split())
li=[int(i) for i in input().split()]
if n1==1:
    print(min(li))
elif n2==2:
    print(max(li[0],li[n1-1]))
else:
    print(max(li))
