#a
n = int(input())
li = list(map(int,input().split()))
li1 = li[:(len(li)//2)]
li2 = li[(len(li)//2):]
li1 = li1[::-1]
li2 = li2[::-1]
for i in range(len(li1)):
  print(li1[i],end = " ")
for i in range(len(li2)):
  print(li2[i],end = " ")
