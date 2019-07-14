#a
a, b = list(map(int,input().split()))
bi = bin(a*b)
x = 0
c = 0
for i in range(2,len(bi)):
  c += 1
  if bi[i] == '1' and x == 0:
    x = 1
    continue
  if bi[i] == '1' and x == 1:
    print(c)
    break
