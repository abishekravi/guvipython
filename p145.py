#a
ax1=int(input())
a1=list(map(int,input().split()))
for i in range(0,ax1-1):
    if a1[i+1]-a1[i]==1:
        print('yes')
        break
else:
    print('no')
