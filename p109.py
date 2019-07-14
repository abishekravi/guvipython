#a
n=int(input())
li=list(map(int,input().split()))
li1=[]
li2=[]
for i in range(0,n):
    li1=li[:i]
    li2.append(sum(li1))
li2.append(sum(li))
li2=li2[1:]
print(*li2[::-1])
