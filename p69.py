#a
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(k):
    l.pop()
print(sep=" ",*l)
