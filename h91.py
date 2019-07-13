#a
s=input()
n=1
if len(s)==1:
    print("yes")
else:
    for j in s:
        if s.count(j)==len(s):
            print("no")
            n=0
            break
    if n==1:
        print("yes")
