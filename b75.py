#a
g=input()
n=len(g)
if n%2!=0:
    g=g[:int(n/2)]+'*'+g[int(n/2)+1:n]
else:
    g=g[:int(n/2)-1]+'**'+g[int(n/2)+1:n]
print(g)
