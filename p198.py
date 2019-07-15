#a
N=int(input())
a=list(map(int,input().split()))
b=sorted(a)
print(a.index(b[len(b)-1])-a.index(b[0]))
