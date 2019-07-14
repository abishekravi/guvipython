#a
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range (n):
  for j in range(0,n):
    b.append(a[i] | a[j])
print(max(b))
