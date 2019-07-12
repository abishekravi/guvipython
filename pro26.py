#a
    
m=input()
b =[int(s) for s in input().split()]
n=[]
for i in range(len(b)):
    n.append(1)

for i in range(len(b)):
    for j in range(i):
        if(b[i]>b[j])and(not(max(n[i],n[j])>n[j])):
            n[i]=n[i]+1
print(max(n))
