#a
n1=int(input())
li=list(map(int,input().split()))
c=sorted(li)
d=c[::-1]
e=[]
for i in range(0,len(li)):
  e.append(d[i])
  e.append(c[i])
for j in e[:len(li)]:
  print(j,end=" ")
