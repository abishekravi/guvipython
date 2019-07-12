#a
    
n,k = map(int,input().split())
l = list(map(int,input().split()))
l = sorted(l,reverse =True)
print(l[k-1])
