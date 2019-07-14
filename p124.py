#a
n = int(input())
li = list(map(int,input().split()))
x = 1
while True:
  t = 0
  for i in range(n):
    if x%li[i] == 0:
      continue
    else:
      t += 1
  if t == 0:
    print(x)
    break
  else:
    x += 1
