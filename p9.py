#a    
y,s=list(map(int,input().split()))
ys=0
for i in range(y,s+1):
    if i>1:
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            ys+=1
print(ys)
