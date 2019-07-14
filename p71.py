#a
a=int(input())
l=list(map(int,input().split()))
l.append(-1)
li=[]
for i in range(a-1):
    li.append(max(l[i],l[i+1]))
if(a==1):
    print(l[0])
else:
    for i in range(len(li)-1):
        print(li[i],end=' ')
    print(li[len(li)-1])
