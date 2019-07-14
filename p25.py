#a
    
a2=int(input())
a3=input().split()
a1=[]
for i in a3:
  a1.append(i)
a1.sort()
a1.sort(key=len)
for i in a1:
  print (i,end=' ')
