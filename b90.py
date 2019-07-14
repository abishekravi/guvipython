#a
x=input()
p=[]
for i in x:
    if(i.isnumeric()):
        p.append(i)
print(''.join(p))
