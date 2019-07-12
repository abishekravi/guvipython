#a
count=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
#print(arr)
sum=0
sum1=0
res=[]
for i in range(0,count,2):
    sum=sum+arr[i]
for j in range(1,count,2):
    sum1=sum1+arr[j]
res.append([sum,sum1])
#print(res)
for i in res:
    print(i[0] if i[0]>i[1] else i[1])
