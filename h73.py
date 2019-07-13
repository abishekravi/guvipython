#a
s=input()
a=input()
k=min(len(s),len(a))
l=""
if k==len(s):
    for i in range(k-1):
        for j in range(i+1,k):
            if s[i:j+1] in a:
                if len(s[i:j+1])>=len(l):
                    l=s[i:j+1]
else:
    for i in range(k-1):
        for j in range(i+1,k):
            if a[i:j+1] in s:
                if len(a[i:j+1])>=len(l):
                    l=a[i:j+1]
print(l)
