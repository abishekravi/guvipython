#a
import math
n1,n2=map(int,input().split())
a=math.factorial(n1)
b=math.factorial(n1-n2)
c=math.factorial(n2)
b=b*c
print(int(a/b))
