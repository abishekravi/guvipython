#a
n=int(input())
li1=[int(i) for i in input().split()]
li2=[int(j) for j in input().split()]
a=li1.index(li1[n-2])
b=li2.index(li1[a])
print(a-b)
