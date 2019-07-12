#abishek    
num1=list(map(str,input()))
set1=cs=0
for i in range(0,len(num1)-1):
  q=num1[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+num1[j]
    if int(q)<27 and int(q)>0: set1=set1+1
    elif int(q)==0: set1=set1-1
    else: break
if set1!=1: cs=set1%2
print(set1+cs+1)
