#a
n=int(input())
li=list(map(int,input().split()))
li1=[]
if(li==sorted(li)):
    for i in li:
        li1.append(li.index(i)+1)
    print(*li1)
else:
    for i in li:
        li1.append(li.index(i)+1)
    print(*li1[::-1])
