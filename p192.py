#a
N=int(input())
a=list(map(int,input().split()))
for i in range(0,N-1):
    if i%2==0 and a[i]>=a[i+1]:
        print('no')
        break
    elif i%2!=0 and a[i]<=a[i-1]:
        print('no')
else:
    print('yes')
