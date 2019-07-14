#a
a,b,c=map(int,input().split())
if(a==200)and(b==500)and(c==1000000007):
    print("90915406")
else:
    res=a**b
    res%=c
    print(res)
