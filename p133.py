#a
n, m = list(map(int,input().split()))
x = 0
for i in range(n):
  a, b = list(map(int,input().split()))
  if b-a > 0 and b-a <= m:
    x = 1
  else:
    break
if x == 1:
  print("yes")
else:
  print("no") 
