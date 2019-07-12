from itertools import combinations
N,k=map(int,input().split())
a=len(str(N))
lst=list(combinations(str(N),a-k))
lst=sorted(lst)
print(*lst[0],sep='')
