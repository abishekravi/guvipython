#a
s=input()
n=len(s)

def check_palindrome(s,n):
    if s==s[-1:-n-1:-1]:
        n-=1
        s=s[0:n]
        check_palindrome(s,n)
    else:
        print(s)


check_palindrome(s,n)    


    
