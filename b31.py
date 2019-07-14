#a
a=list(input())
b=" "
for i in range(len(a)):
    if b in a:
        a.remove(b)
print(len(a))
