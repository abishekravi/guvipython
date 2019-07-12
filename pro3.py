a,b=input().split()
char=abs(len(b)-len(a))
for g in range(len(a)):
  if(len(b)==1 and b[g] in a):
    break
  if(a[g]!=b[g]):
    char=char+1
print(char)
