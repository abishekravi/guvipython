#a
n1=int(input())
li=[]
a=n1//2+n1
for i in range(1,n1+1):
    if i%2==0:
        li.append(i)
for i in range(1,n1+1):
    if i%2!=0:
        li.append(i)
for i in range(1,n1+1):
    if i%2==0:
        li.append(i)
print(a)
print(*li)
