#a
a1,b1=input().split()
a1=int(a1)
b1=int(b1)
s2=''
u1=2
if(a1+b1<=3):
    for i in range(0,a1+b1):
        if(i%2!=0):
            s2=s2+'0'
        else:
            s2=s2+'1'
else:    
    for i in range(0,a1+b1):
        if(i==u1):
            s2=s2+'0'
            if(u1==b1):
                u1=u1+2
            else:
                u1=u1+3
        else:
            s2=s2+'1'
x1=len(s2)-1
if(int(s2[x1])==0):
    print('-1')
elif a1==1 and b1==2: print("011")
else:
    print(s2)
