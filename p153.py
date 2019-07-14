#a
s, n = list(map(str,input().split()))
n = int(n)
for i in range(n-1,len(s),n):
  print(s[i],end = " ")
