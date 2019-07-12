#a
vf,vk=map(int,input().split())
sk=[]
for i in range(0,vf):
    mn=[int(sv) for sv in input().split()]
    sk.append(sorted(mn))
for i in range(0,len(sk[0])):
  #print(sk[i])
  for j in range(0,len(sk)-1):
    if sk[j][i]>sk[j+1][i]:
      sk[j][i],sk[j+1][i]=sk[j+1][i],sk[j][i]
for i in sk:
  print(*i)
