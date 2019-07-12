#a
b,s=map(str,input().split("|"))
c=input()
if  len(b)>len(s):
    if len(b)==len(s)+len(c):
        print(b+"|"+s+c)
elif len(b)<len(s):
     if len(s)==len(b)+len(c):
        print(b+c+"|"+s)
elif len(b)==len(s) and len(c)>1 or (len(s) or len(b)):
    print("impossible")
