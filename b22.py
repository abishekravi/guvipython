#a
num1=int(input())
lst=list(map(int,input().split()))[:num1]
lst.sort()
print(lst[-1])
