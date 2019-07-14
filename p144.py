#a
n = int(input())
li = list(map(int,input().split()))
for i in range(1,n):
  if li[i]%li[i-1] == 0:
    print(li[i],end = " ")
