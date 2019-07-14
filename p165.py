#a
N,k=map(int,input().split())
l=[int(x) for x in input().split()]
l.sort()
for i in l:
    if i>k:
        print(i)
        break
