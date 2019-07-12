#a
os=input()
ls=[]
for i in os:
    if i not in ls:
        ls.append(i)
        #print(i)
    else:
        break
print(len(ls))
