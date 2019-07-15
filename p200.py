#a
N=list(input())
lis=[]
for i in N:
  if i not in lis:
    lis.append(i)
for i in lis:
  print(i,end="")
