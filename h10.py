#a
n,m=map(int,input().split())
l1=list(input().split())
l2=list(input().split())
if set(l2) <= set(l1):
    print("YES")
else:
    print("NO")
