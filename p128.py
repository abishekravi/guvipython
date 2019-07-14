#a
n = int(input())
li = list(map(int,input().split()))
m = 1
for i in range(n):
  m *= li[i]
if m%2 == 0:
  print("even")
else:
  print("odd")
