#a
s = input()
x = 1
for i in range(len(s)):
  if s[i] != 'a' and s[i] != 'b':
    x = 0
    break
if x == 1:
  print("yes")
else:
  print("no")
