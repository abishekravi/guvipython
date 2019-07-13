#a
N=input()
temp=""
f=0
for i in range(len(N)):
  if N[i]==" ":
    temp+=N[i]
  elif f==0:
    temp+=N[i].upper()
    f=1
  elif f==1:
    temp+=N[i]
    f=0
print(temp)
