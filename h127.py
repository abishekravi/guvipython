#a
st1,st2=input().split()
for i in st1:
    for j in st2:
        if(i==j):
            res=set(j)
            print(*res,end="")
