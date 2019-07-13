#a
sm = int(input())
lr = list(map(int,input().split()))
for i in range(len(lr)-1):
    if lr[i]>lr[i+1]:
        print(lr[i+1],end=" ")
    else:
        print(-1,end=" ")
print(-1)
