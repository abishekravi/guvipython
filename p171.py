#a
N=input().split()
for i in range(0,len(N)):
    if len(N)<3:
        break
    if N[i]=='and':
        t=N[i-1]
        N[i-1]=N[i+1]
        N[i+1]=t
print(*N)
