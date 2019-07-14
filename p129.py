#a
n = int(input())
li = list(map(int,input().split()))
li1 = [0]
for i in range(n):
  s = 0
  for j in range(i,n):
    s += li[j]
    li1.append(s)
print(min(li1))
