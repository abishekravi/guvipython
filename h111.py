#a
n=int(input())
a=0
li=[[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    a+=li[i][(n-1)-i]
print(a)
