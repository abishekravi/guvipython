#a
from itertools import permutations
p=input()
q=permutations(p)
r=[]
for i in list(q):
        s="".join(i)
        if s not in r:
             r.append(s)
for i in r:
      print(i)
