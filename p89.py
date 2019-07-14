#a
import math
n1,n2=map(int,input().split())
a=math.factorial(n1)
b=math.factorial(n1-n2)
print(int(a/b))
