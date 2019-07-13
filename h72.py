#a
s=input()
s=s.replace(".","")
l=s.split()
k=""
for i in range(1,len(l)+1):
    if i%2!=0:
        k=k+l[i-1][::-1]+" "
    else:
        k=k+l[i-1]+" "
print(k.strip())        
#rev_at_odd
