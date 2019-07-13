#a
def LIS(arr,size):
    res=[]
    count=1
    for i in range(0,size-1):
        if arr[i]<arr[i+1]:
            count+=1
        else:
            res.append(count)
            count=1
    res.append(count)
    print(max(res))
size=int(input())
arr=list(map(int,input().split()))
LIS(arr,size)
