#a
nn = int(input())
ll = list(map(int, input().split()))
maximum = 0
cnt = 0
for i in range(nn-1):
    if ll[i] < ll[i+1]:
        cnt +=1
        if maximum < cnt:
            maximum = cnt
    else:
        cnt = 0
print(maximum+1)
