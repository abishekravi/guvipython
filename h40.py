#a
    
n=input()
li=list(map(int,n))
nsum=sum(li)
nsum=str(nsum)
rev=nsum[::-1]
if(nsum==rev):
    print("YES")
else:
    print("NO")
