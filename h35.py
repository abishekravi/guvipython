#a
t=input()
a1=0
for i in range(len(t)):
    if t[:i]==t[i+1:]:
        a1=0
        break
    else:
        a1=1
if a1==0:
    print("YES")
else:
    print("NO")
