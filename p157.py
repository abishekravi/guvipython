#a
a, b = list(map(int,input().split()))
b = bin(a*b)
for i in range(2,len(b)):
  if b[i] == '1':
    print(i+1)
    break
