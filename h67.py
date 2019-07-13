#a
a=input().split("#")
b=input().split("#")
d=a[1]+a[2]+a[3]
e=b[1]+b[2]+b[3]
if d>e:
    print(a[0])
elif e>d:
    print(b[0])
