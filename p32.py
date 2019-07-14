#a
n,l=map(int,input().split())
k=list(map(int,input().split()))
for i in k:
    if(i==l):
        print("Yes")
        break
else:
    print("No")
