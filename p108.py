#a
num=int(input())
li=list(map(int,input().split()))
li1=[]
for i in range(0,num):
    su=0
    for j in range(0,i+1):
        su=su+li[j]
    li1.append(su)
print(*li1)
