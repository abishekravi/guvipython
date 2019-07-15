#a
N=int(input())
l=[]
s=1
k=1
for i in range(0,N):
    l.append(list(map(int,input().split())))
for i in range(0,N):
    for j in range(0,N):
        if i==j:
            s=s*l[i][j]
        if i+j==N-1:
            k=k*l[i][j]
print(s+k)
