#a
s=input()
l=[0]
if "ab" not in s:
	print("0")
else:
	for i in range(len(s)):
		c=1
		for j in range(i,len(s)-1):
			if s[j]=="a" and s[j+1]=="b":
				c=c+1
			elif s[j]=="b" and s[j+1]=="a":
				c=c+1
			else:
				l.append(c)
				c=1
				break
		if s[i]=="a":
			l.append(c)
		else:
			l.append(c-1)
	print(max(l))
