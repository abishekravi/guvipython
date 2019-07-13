#a
n1=int(input())
li=list(map(int,input().split()))
x=0
for i in range(n1):
    if(sum(li[:i])==sum(li[i+1:])):
        x=x+1
if x>0:
    print("yes")
else:
    print("no")
