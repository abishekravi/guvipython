#a
x=int(input(""))
li=list(map(int,input().split()))[:x]
max=0
mi=0
if(x==1):
    mi=1
    print(mi)
else:
    
    for i in range(0,len(li),1):
        k=li.count(i)
        if(k==1):
            mi+=i   
            print(mi)
            break
