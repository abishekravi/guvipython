#a
ax=list(map(int,input()))
c=0
a=[]
for i in range(0,len(ax)-1):
    if (ax[i]%2==0 and ax[i+1]%2!=0) or(ax[i]%2!=0 and ax[i+1]%2==0):
        c=c+1
        a.append(c)
    else:
        c=0
a.append(c)
if max(a)==0:
    print(max(a))
else:
    print(max(a)+1)
