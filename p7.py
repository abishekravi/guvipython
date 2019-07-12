#a
sv=input()
sv=list(sv)
res=""
for i in range(0,len(sv)-1,2):
    temp=sv[i+1]
    sv[i+1]=sv[i]
    sv[i]=temp
print(res.join(sv))
