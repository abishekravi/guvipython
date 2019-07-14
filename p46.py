#a
import math
angle=int(input())
b=math.radians(angle)
y=math.sin(b)
if(b<1):
    print(round(y,1))
elif(b>1):
    print(round(y))
