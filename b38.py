#a
ln=list(map(int,input().split()))
a=ln[0]
b=ln[1]
a=a^b
b=a^b
a=a^b
print(a,b)
