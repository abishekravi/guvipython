#a
x,y=map(int,input().split())
z=x*y
s=z*z
if(s%x==0):
    print("yes")
else:
    print("no")
