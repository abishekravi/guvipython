#a
N=input()
k=""
m=0
for i in range(len(N)-1):
    k=""
    if N[i]==N[i+1]:
        k=k+N[:i+1]+N[i+2:]
        if int(k)>m:
            m=int(k)
print(m)
