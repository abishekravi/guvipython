#a
N=int(input())
n=0
for i in range(N+1):
    s=str(i)
    if all(abs(int(s[j])-int(s[j-1]))==1 for j in range(1,len(s))):
        n=n+1
print(n)
