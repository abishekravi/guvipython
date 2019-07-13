#a
N = input()
c,n,m = 0,'',0
for i in range(0,len(N)):
  c = 1
  for j in range(i+1,len(N)):
    if N[i]==N[j]:
      c += 1
    else:
      break
  if c>m:
    m = c
    n = N[i]
print(n,m)
