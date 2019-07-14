#a
n=int(input())
li=list(map(int,input().split()))
su=0
for i in range(n-1):
    su+=li[i]+li[i+1]
print(su)
