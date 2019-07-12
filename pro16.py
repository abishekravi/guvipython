#a
a1=int(input())
c=list(map(int,input().split()))
y=[1]*a1
for i in range(a1):
    if i==0:
        if c[i]>c[i+1]:
            y[i]=y[i]+y[i+1]
    elif i>0:
        if c[i]>c[i-1]:
            y[i]=y[i]+y[i-1]
print(sum(y))
