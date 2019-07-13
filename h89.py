#a
X=str(input())
t=[]
for i in range(0,len(X)):
    if(X[i] not in t):
         t.append(X[i])
t=t[::-1]
print(*t,sep="")
