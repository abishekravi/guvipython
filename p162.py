#a
N =list(map(int,input().split()))
a2 = []
a3 = ['a','e','i','o','u']
k=0
for i in range(0,N[0]):
    a2.append(list(input()))

    for j in a2[i]:
        if j in a3:
            k = k+1
            break

if k >= N[1]:
    print("yes")
else:
    print("no")
