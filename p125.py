#a
n = int(input())
li = list(map(int,input().split()))
li1 = li[:]
li1.sort()
li1 = li1[::-1]
for i in range(n):
  x = 0
  for j in range(n):
    if li[j]%li1[i] == 0:
      continue
    else:
      x += 1
  if x == 0:
    print(li1[i])
    break
