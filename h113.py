#a
N=int(input())
if N==1:
    print("YES")
elif N%2!=0:
    print("NO")
else:
    while N%2==0:
        N=N//2
    if N==1:
        print("YES")
    else:
        print("NO")
