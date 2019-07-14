#a
s = input()
x = 0
for i in range(len(s)):
  if s[i] != 'a' and s[i] != 'b':
    x += 1
if x == 0 or x == 1:
  print("yes")
else:
  print("no")
