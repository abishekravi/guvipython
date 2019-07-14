#a
import math
a,b=map(int,input().split())
count=0
for i in range(a,b+1):
    c=math.sqrt(i)
    if(c-math.floor(c)==0):
        count=count+1
print(count)
