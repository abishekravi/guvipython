#a
n=int(input())
li=[int(i) for i in input().split()]
for i in range(0,n):
    for j in range(i+1,n):
        a=li[i]^li[j]
print(a)
