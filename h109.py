#a
X=int(input())
Y=list(map(str,input().split()))[:X]
l=[]
t=[]
for i in range(0,len(Y)):
    l.append(Y[i].lower())
for i in range(0,X):
      m=min(l)
      t.append(m)
      l.remove(min(l))
for i in t:
    print(i)
