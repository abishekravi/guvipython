from itertools import combinations
n,k=map(int,input().split())
a=len(str(n))
lst=list(combinations(str(n),a-k))
lst=sorted(lst)
print(*lst[0],sep='')
