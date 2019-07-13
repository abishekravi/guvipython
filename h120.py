#a
x=int(input())
ar=list(map(int,input().split()))[:x]
ct=0
for i in range(0,x-2):
    for j in range(i+1,x-1):
        for k in range(i+2,x):
            if(ar[i]+ar[j])==ar[k] :
                ct+=1           
print(ct)
