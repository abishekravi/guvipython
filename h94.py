#a
a=input().split()
b=[]
for i in a:
  b.append(i[::-1])
print(*b)
