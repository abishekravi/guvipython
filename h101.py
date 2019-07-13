#a
N=int(input())
a=[]
c=0
for i in range(2,N):
    for j in range(2,i+1):
        if i%j==0:
            break
    if j==i:
        a.append(i)
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if a[i]+a[j]+a[k]==N:
                print(str(a[i])+" "+str(a[j])+" "+str(a[k]))
                c=1
                break
        if c==1:
            break
    if c==1:
        break
