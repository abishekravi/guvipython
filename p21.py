#a
x,y=list(map(int,input().split()))
i,j=list(map(int,input().split()))
k,l=list(map(int,input().split()))
if(x==i==k) or (y==j==l) or (x==y and i==j and k==l):
    print("yes")
