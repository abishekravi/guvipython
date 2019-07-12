#a
    
sh=int(input())
me=list(map(int,input().split()))
me.sort()
sin=0
se=0
for i in range(len(me)):
    if me[i]>=sin:
        se=se+1
    sin=sin+me[i]
print(se)
