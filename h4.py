N1=int(input())
s1=list(map(int,input().split()))
t1=[]
for i in s1:
    if s1.count(i)==1:
        if i not in t1:
            t1.append(i)
print(*t1)
