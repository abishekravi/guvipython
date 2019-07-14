#a
n = int(input())
b = str(bin(n))[2:]
x = 0
for i in range(len(b)-1,-1,-1):
  if b[i] is '1':
    x += 1
print(x)
