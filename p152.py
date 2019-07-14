#a
saa=input()
ca=0
la=["a","e","i","o","u"]
for i in range(0,len(saa)-2):
	if saa[i] in la and saa[i+1] not in la:
		ca+=2
		if saa[i+1] not in la and saa[i+2] in la:
			ca+=1
print(ca)
