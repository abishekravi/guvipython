#a
n=int(input())
li=[]
a=0
for i in range(2,n):
    s=0
    for j in range(2,i):
        if(i%j==0):
            s=1
    if(s==0): 
        li.append(i)
for i in range(0,len(li)):
    if(li[i]==3 or li[i]%10==3):
        a=a+li[i]
print(a)
