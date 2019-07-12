#a
s=input()
s=s.split()
s1=s[0]
s2=s[1]
count=0
i=0
while(i<len(s1) and count<2):
    if(s1[i]!=s2[i]):
        count+=1
    i+=1
if(count==1 or count==0):
    print("yes")
else:
    print("no")
