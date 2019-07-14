#a
nv,bv,s33=map(int,input().split())
sen=0
for k in range(0,s33):
   sen=sen+nv
   nv=nv+bv
print(sen)
