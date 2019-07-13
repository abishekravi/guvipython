#a
def compute_gcd(n1,n2):   #compute the gcd
    while(n2):
        n1,n2=n2,n1%n2      

    return n1

def compute_lcm(n1,n2):   
    lcm=(n1*n2)//compute_gcd(n1,n2)   #compute the lcm
    return lcm

inp=list(map(int,input().split()))  
print(compute_lcm(inp[0],inp[1]))
