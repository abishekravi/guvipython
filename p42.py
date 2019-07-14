#a
num=int(input())
a=input().split(" ")
list1=[]
if(len(a)==num):
    for i in sorted(a):
        list1.append(i)
if(list1==a):
    print("yes")
else:
    print("no")
