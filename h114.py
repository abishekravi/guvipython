#a
def PSUM(n) :
    sum1 = 0
    while n :
        sum1 += n%10
        n //= 10
    return sum1

def isPrime(n) :
    if n==1 : return False
    if n==2 or n==3 : return True
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

a,b = input().split()
a,b = int(a),int(b)
out = 0
for i in range(a,b+1) :
    sum1 = PSUM(i)
    if isPrime(sum1) :
        out += 1
        
print(out)
