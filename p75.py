#a
n1=int(input())
l=[int(i) for i in input().split()]
c=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]<l[j]):
            c=c+1
print(c)
