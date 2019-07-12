#a
a,b,c,d=map(int,input().split())
list1=list(map(int,input().split()))
list2=[]
for i in range(0,len(list1)):
    for j in range(i,len(list1)):
        for k in range(j,len(list1)):
            list2.append(b*list1[i]+c*list1[j]+d*list1[k])
print(max(list2))
