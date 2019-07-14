#a
    
c=input()
l1=len(c)
count=0
for i in range(0,l1):
    if(c[i]=="("):
        count=count+1
    elif(c[i]==")"):
        count=count-1
if(count==0):
    print("yes")
else:
    print("no")
