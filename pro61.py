#a
st1=input()
st2=input()
a=[]
b=[]
c=[]
for i in st1:
    a.append(ord(i)-ord('a'))
for i in st2:
    b.append(ord(i)-ord('a'))
for i,j in zip(a,b):
    c.append((chr((i+j)%26+ord('a')+1)))
print("".join(c))
