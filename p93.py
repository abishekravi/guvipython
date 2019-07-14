#a
n=int(input())
li1=[int(i) for i in input().split()]
for i in range(0,n-1,2):
    li1[i],li1[i+1]=li1[i+1],li1[i]
print(*li1)
