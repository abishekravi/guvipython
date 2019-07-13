#a
n1,n2=map(int,input().split())
li=[str(i) for i in input().split()]
a=li[n2:]+li[:n2]
print(' '.join(a))
