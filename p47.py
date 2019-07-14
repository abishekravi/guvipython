#a
an1,an2,an3=map(int,input().split(" "))
if(an1!=0 and an2!=0 and an3!=0):
    a=an1+an2+an3
else:
    a=0
if(a==180):
    print("yes")
else:
    print("no")
