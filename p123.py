#a
n=int(input())
f=0
l=[]
l1=[]
for i in range(2,n):
    if(n%i==0):
        l.append(i)
for i in range(len(l)):
    for j in range(2,l[i]):
        if(l[i]%j==0):
            l1.append(l[i])
            break
for i in l:
    if(i not in l1):
        print(i,end=" ")
