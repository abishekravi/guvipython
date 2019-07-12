#a
k,m=map(int,input().split())
mk=list(map(int,input().split()))
l1=[]
for i in range(0,m):
     a,b=map(int,input().split())
     l1.append([a,b])
for i in range(m):
     lower=l1[i][0]
     upper=l1[i][1]
     x=sum(mk[lower-1:upper])
     print(x)
