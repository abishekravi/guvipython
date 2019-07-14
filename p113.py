#a
s1 = input()
if len(s1) is 10 and s1[2] is '/' and s1[5] is '/':
  dd = int(s1[:2])
  mm = int(s1[3:5])
  yy = int(s1[6:])
  if dd >= 1 and dd <= 31 and mm >= 1 and mm <= 12:
    print("yes")
  else:
    print("no")
else:
  print("no")
