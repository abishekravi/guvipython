#a
inp=int(input())

ii=0

xy=0

b=[]

while ii<90 and ii<inp:

  s=0

  for j in str(inp-ii):

    s+=int(j)

  if s+(inp-ii)==inp:

    xy+=1

    b.append(inp-ii)

  ii+=1

print(xy)

for ii in b:

  print(ii)
