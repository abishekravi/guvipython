#a
n1=int(input())
s=str(input())
a=""
r=""
for i in range(len(s)):
    if s[i]=='1':
        a=a+s[i]+" "
    elif s[i]=='0':
        r=r+a
        a=""
print(r.strip())
