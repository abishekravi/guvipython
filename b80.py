#a
X=input()
t=[]
for i in range(0,len(X)):
        if(int(X[i])%2==1):
           t.append(X[i])
print(*t,end="")
