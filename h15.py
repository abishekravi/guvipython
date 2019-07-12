#a
n=int(input())
l=list(map(int, input().split()))[:n]
mx=max(l)
fnl=[]
for i in range(0,len(l)):
    new=l[i:]
    fi=max(new)
    if(l[i]==fi):
        fnl.append(l[i])
print(*fnl)
print(mx)
