#a
jk=int(input())
SUM=0
lm=str(jk)
h=[]
for i in range(0,len(lm)):
    SUM=SUM+int(lm[i])
    h.append(SUM)
print(sum(h))
