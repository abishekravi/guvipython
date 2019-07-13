#a
import sys,string
def dgtSum(n) :
    sum1 = 0
    while n :
        sum1 += n%10
        n //= 10
    return sum1

n = int(input())
if n <= 9:
    print(n)
    sys.exit()
a = n // 9
b = n % 9
if b :
    s = str(b) + str('9') * a
else :
    s = str('9') * a
print(s)
