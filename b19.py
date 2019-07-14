#a
x=int(input())
sum=1
if(x==0):
    print("1")
else:
    for i in range(1,x+1):
        sum=sum*i 
    print(sum)
