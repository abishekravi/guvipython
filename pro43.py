#a
    
thi = int(input())
aa1 = list(map(int,input().split()))
ss,l = 0,[]
b1 = [x for x in range(1,thi+1)]
for i in aa1:
  if i in b1:
    b1.remove(i)
kh = 0
for i in range(0,thi-1):
  p = aa1[i]
  for j in range(i+1,thi):
    if p == aa1[j]:
      if p < b1[kh]:
        aa1[j] = b1[kh]
        ss += 1
      else:
        aa1[i] = b1[kh]
        ss += 1
      kh += 1
print(ss)
print(*aa1)
