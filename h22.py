#a
new=int(input())
l1=list(map(int,input().split()))
rem=1
l=[]
for i in l1:
  rem=rem*i
for i in l1:
  l.append(rem//i)
print(*l)
