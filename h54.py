#a
n=int(input())
li=list(map(int,input().split()))
li2=[]
for i in range(0,n):
    li2.append(li[i])
    print(min(li2),end=" ")
