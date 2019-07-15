#a
from itertools import permutations
N=input()
l=list(permutations(N))
c=0
for i in range(len(l)):
	if l[i]==l[i][::-1]:
		c=1
		print("yes")
		break
if c==0:
	print("no")
