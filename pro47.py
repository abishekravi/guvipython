#a
a,b=map(int,input().split())
if a%10==0:
  a=str(a)
  c=0
  for i in range(len(a)-1,-1,-1):
    if a[i]=='0':
      c+=1
  if b<=c:
    print(a)
  else:
    a=a[:-c]
    a=a+'0'*b
    print(a)
elif 10%(a%10)==0:
  no=int('1'+'0'*b)
  while True:
    if no%a==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*b)
else:
  print(str(a)+b*'0')
