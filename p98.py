#a
n1,n2=map(str,input().split())
n1=list(n1)
n2=int(n2)
j=-1
for i in range(0,n2+1):
    if(str(i) in n1): 
      j=j+1
if(j==n2): 
  print("yes")
else: 
  print("no")
