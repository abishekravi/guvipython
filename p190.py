#a
A,B,C=map(int,input().split())
if (A**2)+(B**2)==C**2 or (B**2)+(C**2)==A**2 or (A**2)+(C**2)==B**2:
	print("yes")
else:
	print("no")
