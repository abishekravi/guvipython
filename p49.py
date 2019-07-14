#a
z1=int(input())
if(z1>=-2**15+1 and z1<=2**15+1):
  print('INT')
elif(z1>=-2**31+1 and z1<=2**31+1):
  print('LONG')
else:
  print('LONG LONG')  
