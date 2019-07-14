#a
    
n=int(input())
l=[int(i) for i in input().split()]
r=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        t=abs(l[i]-l[j])
        if(t==0):
            continue
        r.append(t)
print(min(r))
