#a
n=int(input())
a=list(map(int,input().split()))
if(len(a)>1):
  b=a[0]&a[1]
else:
  b=a[0]
for i in range (2,n):
    b=b&a[i]
print(b)
