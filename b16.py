#a
m,n=map(int,input().split())
for mo in range(m+1,n):
    if mo>0:
        for i in range(2,mo):
            if mo%i==0:
                break
        else:
            print(mo,end=" ")
