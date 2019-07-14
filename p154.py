#a
s, n = list(map(str,input().split()))
n = int(n)
s1 = ""
if len(s) == 1:
  print(s.upper())
else:
  for i in range(0,len(s),n):
    for j in range(i,i+n-1):
      s1 += s[j]
    s1 += s[i+n-1].upper()
  print(s1)
