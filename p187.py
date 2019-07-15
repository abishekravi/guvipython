#a
N=input().split()
a=len(N[0])
b=len(N[1])
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        m=i
if m==1:
    print('yes')
else:
    print('no')
