#a
a1=int(input())
a2=[]
for i in range(0,a1):
    a2.append(list(map(int,input().split())))
c=0
k=0
for i in range(0,a1):
    for j in range(0,a1):
        if a2[i][j]==1:
            if i!=a1-1 and a2[i+1][j]==0:
                c=c+1
            if j!=a1-1 and a2[i][j+1]==0:
                c=c+1
            if i!=0 and a2[i-1][j]==0:
                c=c+1
            if j!=0 and a2[i][j-1]==0:
                c=c+1
            if i==0 and j==0 or i==a1-1 and j==a1-1  or i==0 and j==a1-1 or i==a1-1 and j==0 and c==2:
                k=k+1
            elif i==1 and j>0 and j<d-1 and c==3:
                k=k+1
            elif c==4:
                k=k+1
        c=0
                
print(k)
