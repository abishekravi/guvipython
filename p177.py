#a
N=list(map(str,input().split()))
a=[]
for i in N:
    k=sorted(i)
    a.append(k)
for i in range(len(a)):
    for j in a[i]:
        print(j,end="")
    if i!=len(a)-1:
        print(" ",end="")
