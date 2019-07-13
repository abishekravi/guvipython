#a
n1=int(input())
l1=[int(x) for x in input().split()]
a1=1000
for i in range(0,len(l1)-1):
    for j in range(i+1,len(l1)):
        if abs(l1[i]+l1[j])<a1:
            a1=abs(l1[i]+l1[j])
            r1,g1=l1[i],l1[j]
print(r1,g1)
