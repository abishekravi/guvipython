#a
n = int(input())
n = str(n)
s = 0
for i in range(len(n)):
  if int(n[i])%2 == 1:
    s += int(n[i])
if s%2 == 0:
  print("E")
else:
  print("O")
