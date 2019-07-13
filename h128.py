#a
st=input()
a=[]
for i in range(0,len(st)):
    for j in range(len(st)-1,i,-1):
        if(st[i]==st[j]):
            x=st[i:j+1]
            if(x==x[::-1]):
                a.append(x)
a=sorted(a)
for i in range(0,len(a)):
    print(a[i])
