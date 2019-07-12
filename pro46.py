#a
th=int(input())
sh=list(map(int,input().split()))
a=0
b=0
sh.sort(reverse=True)
for i in sh:
  sh=a+i
  if b>sh:
    a=sh
  else:
    a=b
    b=sh
print(a,b)
