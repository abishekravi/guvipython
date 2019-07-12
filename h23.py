#a
n,m=map(eval,input().split())
a=[]
for i in range(n):
  a.append(list(map(eval,input().split())))
pos=[]
out=[]
temp_out=[]
t=[]
i=0
j=0
out.append(a[i][j])
pos.append([i,j])
while [n-1,m-1] not in pos:
  i=0
  for x in pos:
    if x[0]+1<n and x[1]+1<m:
      temp_out.append(a[x[0]+1][x[1]]+out[i])
      temp_out.append(a[x[0]][x[1]+1]+out[i])
      t.append([x[0]+1,x[1]])
      t.append([x[0],x[1]+1])
    elif x[0]+1<n:
      temp_out.append(a[x[0]+1][x[1]]+out[i])
      t.append([x[0]+1,x[1]])
    elif x[1]+1<m:
      temp_out.append(a[x[0]][x[1]+1]+out[i])
      t.append([x[0],x[1]+1])
    i+=1
  pos=t
  t=[]
  out=temp_out
  temp_out=[]
print(max(out))
