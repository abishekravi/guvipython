#a
number=int(input())
li=list(map(str,input().split()))
numbertofind=input()
count=0
for value in li:
  if numbertofind==value[0:2]:
    count+=1
print(count)
