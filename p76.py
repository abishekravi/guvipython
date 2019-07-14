#a
n=int(input())
a=list(map(int,input().split()))
ecount=evalue=0
ocount=ovalue=0
for i in a:
  if(i%2==0):
    ecount=ecount+1
    evalue=i
  else:
    ocount=ocount+1
    ovalue=i
if(ecount==1):
  print(evalue)
else:
  print(ovalue)
