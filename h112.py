#a
n1=list(map(str,input()))
n2=list(map(str,input()))
li=[]
for i in range(0,len(n1)):
    for j in range(0,len(n2)):
        if(n1[i]==n2[j] and j<=i):
            if(n1[i] not in li): 
                li.append(n1[i])
for i in range(0,len(li)):
    print(*li[i],end="")
