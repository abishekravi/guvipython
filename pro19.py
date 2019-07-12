count1=int(input())
array=[]
ss=[]
for i in range(count1):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        ss.append(num)
ss.sort()
for i in ss:
    print(i,end=' ')
    #a
