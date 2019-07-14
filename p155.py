#a
n, k = list(map(int,input().split()))
li = list(map(int,input().split()))
li1 = li[:k]
li2 = li[k:]
li1.sort()
li2.sort()
for i in range(len(li1)):
  print(li1[i],end = " ")
for i in range(len(li2)-1,-1,-1):
  print(li2[i],end = " ")
