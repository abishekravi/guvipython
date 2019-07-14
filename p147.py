#a
s = list(map(str,input().split()))
if len(s) != 1:
  print(s[0],end = " ")
  for i in range(1,len(s)-1):
    print(s[i][::-1],end = " ")
print(s[-1])
