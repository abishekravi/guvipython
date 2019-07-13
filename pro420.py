#a
tt1,tt2=map(int,input().split())
li=list(map(int,input().split()))
if tt2==1:
  print(min(li))
elif tt2==2:
  print(max(li[0],li[tt1-1]))
else:
  print(max(li))
