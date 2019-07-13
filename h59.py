#a
n=int(input())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
li3=[]
for i in range(n):
               li3.append(li1[i]+li2[i])
print(*li3,end=' ')
