#a
null = input()
l = list(map(int,input().split()))
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if l[i]+l[j] == l[k] and i<j<k:
                print(l[i],l[j],l[k])
