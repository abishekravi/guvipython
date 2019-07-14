#a
n = int(input())
x = 0
for i in range(n):
  if 2**i == n:
    x = 1
    break
if x == 1:
  print("yes")
else:
  print("no")
