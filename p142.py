#a
n, k = list(map(int,input().split()))
li = []
c = []
for i in range(n):
  li.append(input())
for i in range(n-1):
  c.append(li.count(li[i]))
if k in c:
  print("yes")
else:
  print("no")
