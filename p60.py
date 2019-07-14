#a
m=list(input().split())
a=m[0]
b=m[1]
for i in a:
  if(i in b):
    print("yes")
    exit()
print("no")
