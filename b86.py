#a
n=list(input())
a=[]
for i in n:
    if i not in a:
        a.append(i)
if(n==a):
    print("Yes")
else:
    print("No")
