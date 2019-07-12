#a
sbhav,imah=map(int,input().split())
list1=list(map(int,input().split()))
sbhav=[]
list1.insert(0,0)
for y in range(imah):
     vin=[]
     s=0
     bb,zz=map(int,input().split())
     for i in range(bb,zz+1):         
         s^=list1[i]     
     sbhav.append(s)
for y in sbhav:
     print(y)
