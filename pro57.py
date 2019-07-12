#a
az,bx=map(str,input().split())
co=0
for i in range(0,len(az)):
    for j in range(0,len(bx)):
        if az[i]==bx[j]:
            co+=1
if co>=2:
    print("yes")
else:
    print("no")
