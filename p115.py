#a
    
s1, m = list(map(str,input().split()))
l1 = len(s1)
l2 = len(m)
if l1 > l2:
  print(s1[:l2]+m)
elif l1 < l2:
  print(s1+m[:l1])
else:
  print(s1+m)
