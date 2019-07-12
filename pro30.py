#a

n1=input()
ca=0
for i in range(0,len(n1)):
    ss=n1[0:i]+n1[i+1::]
    if int(ss)%8==0:
        ca=1
        break
if ca==1:
    print("yes")
else:
    print("no")
