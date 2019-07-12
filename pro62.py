#a
st1=input()
b=0
c=[]
for i in range(0,len(st1)-1):
    for j in range(i+1,len(st1)):
        k=st1[i:j+1]
        l=k[::-1]
        if k==l:
            c.append(len(st1)-len(l))
print(min(c))
