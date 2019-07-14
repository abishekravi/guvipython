#a
n, l ,r = list(map(int,input().split()))
li = list(map(int,input().split()))
li1 = []
for i in range(n):
  if li[i] >= l and li[i] <= r:
    li1.append(li[i])
print(min(li1))
