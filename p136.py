#a
n, k = list(map(int,input().split()))
li = list(map(int,input().split()))
c = 0
for i in range(n):
  if li[i] is k:
    c += 1
if c == 0:
  print("no")
else:
  print("yes",end = " ")
  print(c)
