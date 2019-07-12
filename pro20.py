#a
x,y=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
a=0
total=y
for i in arr:
    if total>=i:
        rem=int(total/i)
        a+=rem
        total=total - (i*rem)
    if total==0:
        break
if total==0:
    print(a)
else:
    print("it's not possible to sum up coins in such a way that they um upto",y)
