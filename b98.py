#a
ntr=int(input())
nom=list(map(int,input().split()))
for y in range(len(nom)-1):
   if(nom[y]>nom[y+1]):
      print(y)
