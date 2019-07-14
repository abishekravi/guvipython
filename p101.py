#a
n=int(input())
li=list(map(int,input().split()))
f=0
for i in range(0,len(li)-1):
    f=f+max(li[i],li[i+1])
print(f)
