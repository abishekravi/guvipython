#a
r=input()
l=str(input())
v=('a','e','i','o','u')
for i in l:
    if i in v:
        l=l.replace(i,"")
print(l[::-1])
