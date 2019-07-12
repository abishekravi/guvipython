#a
n, m = [int(i) for i in input().split()]
u = []
Lis = [int(i) for i in input().split()]
for _ in range(m):
    l, k = [int(i) for i in input().split()]
    u.append(min(Lis[l-1:k]))
for i in u:
    print(i)
