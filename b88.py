#a
import math
x,y=map(int,input().split())
z=math.gcd(x,y)
lcm=(x*y)/z
print(math.ceil(lcm))
