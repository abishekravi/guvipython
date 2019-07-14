#a
st=input()
rst=input()
l=list(st.split())
l1=[]
for i in range(len(l)):
    if(rst!=l[i]):
        l1.append(l[i])
print(' '.join(l1))
