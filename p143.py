#a
n = int(input())
li = list(map(int,input().split()))
weight = list(map(int,input().split()))
weight1 = weight[:]
weight.sort()
for i in range(n):
  for j in range(n):
    if weight[i] == weight1[j]:
      print(li[j],end = " ")
