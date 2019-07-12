#a
n = int(input())
P = list(map(int,input().split()))
j = 1
miner = sum(P)
ind = 0
while(j<n):
    x = sum(P[:j])
    y = sum(P[j:])
    if(x>y):
        res=x-y
    else:
        res=y-x
    if(res<miner):
       miner = res
       ind = n-j
       t1 = j
    j+=1
print(t1-ind)
