#a
    
st=input()
for i in range(len(st)):
    if(st.count(st[i])==1):
        print(st[i],end="")
