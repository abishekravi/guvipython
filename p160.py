#a
a, b = list(map(int,input().split()))
bi = bin(a | b)
c = 0
for i in range(2,len(bi)):
  if bi[i] == '1':
    c += 1
print(c)
