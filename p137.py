#a
n = int(input())
b = str(bin(n))[2:]
x = 1
for i in range(len(b)-1,-1,-1):
  if b[i] is '0':
    x += 1
  else:
    print(x)
    break
