#a
import sys,string
def cfreq(s) :
    din = {}
    for c in s :
        din[c] = din.get(c,0) + 1
    return din
 
s = input()
n = len(s)
din = cfreq(s)
Lk = list(din.keys())
#print(din,Lk)
 
for j in range(n-2,-1,-1) :
    #print('len = ', j+1)
    for c in Lk :
        kin = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            s2 = s[li:ri + 1]
            #print(c,s2)
            if c in s2 :
                kin += 1
        if kin == n-j :
            #print('c,kin',c,kin)
            c2 = c
            kin2 = kin
            len2 = j+1
print(len2)
