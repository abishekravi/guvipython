#a
n1 = int(input())
li = list(map(int,input().split()))
unique = []
count = []
li.sort()
li = li[::-1]
for i in range(n1):
  if li[i] not in unique:
    unique.append(li[i])
for i in range(len(unique)):
  count.append(li.count(unique[i]))
for i in range(len(count)):
  ind = count.index(max(count))
  print(unique[ind],end = " ")
  unique.remove(unique[ind])
  count.remove(count[ind])
