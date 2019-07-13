#a
    
n=int(input())
li=[]
for i in range(0,n):
    for j in range(i,n):
        li.append("1")
    print(*li)
    li=[]
