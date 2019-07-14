#a
st=str(input())
c=0
for i in range(0,len(st)):
    for k in range(i+1,len(st)):
        if(st[i]==st[k]):
            c+=1 
if(c>=1):
    print("yes")
else:
    print("no")
