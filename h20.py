#a
x,b=map(int,input().split())
l=[]
c=0
k=[]
for i in range(x,b+1):
        l.append(bin(i)[2::])
for i in range(0,len(l)):
        k.append(l[i].count("1"))
 
for i in range(0,len(k)):
        if k[i]!=1 and k[i]!=2:
                for p in range(2,k[i]):
                        if k[i]%p==0:
                                break
                if p==k[i]-1:
                        c=c+1
        elif k[i]==2:
                c=c+1
print(c)
