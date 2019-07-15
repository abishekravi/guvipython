#a
N=input()
n=input()
l=[]
if (N.isalpha() or " " in N) and (n.isalpha() or " " in n):
    N=list(N.split(" "))
    n=list(n.split(" "))
    for i in N:
        if N.count(i) > n.count(i) and i not in l:
            l.append(i)
    for i in n:
        if n.count(i)>N.count(i) and i not in l:
            l.append(i)
    print(*l)
else:
    for i in N:
        if N.count(i)>n.count(i) and i not in l:
            l.append(i)
    for i in n:
        if n.count(i)>N.count(i) and i not in l:
            l.append(i)
    print(*l)
