#a
n = int(input())
li = []
x = 0
for i in range(n):
  li.append(input())
for i in range(n-1):
  for j in range(i+1,n):
    if li[i] == li[j]:
      x = 1
      break
if x == 1:
  print("yes")
else:
  print("no")
