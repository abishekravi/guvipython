#a
a,b=map(int,input().split())
c=a^b
d=bin(c)
C=0
for i in d:
    if i=='1':
        C=C+1 
print(C)
