#a
a=input()
b=input()
c=a+b 
c=list(c)
c.sort()
CIT=0
for K in range(0,len(c)):
    if len(c)<26 or c.count(c[K])>1:
        CIT=CIT+1 
if CIT==0:
    print("complementary")
else:
    print("non-complementary")
