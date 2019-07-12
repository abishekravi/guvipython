#a
    
bhav,mah=map(int,input().split())
zen=list(map(int,input().split()[:mah]))
zig=[]
for i in zen:
   if(i<=i+1):
     zig.append(i)
print(zig[mah-1])  
