#a
n=int(input())
li=[int(i) for i in input().split()]
n2=0
for i in range(0,len(li)):
    if li.count(li[i])>n2:
        n2=li.count(li[i])
        a=li[i]
print(a)
