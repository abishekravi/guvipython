chaa=int(input())
choa=[int(o) for o in input().split(" ")]
chea=0
for p in range(chaa):
      for g in range(p):
           if(choa[g]<choa[p]):
                chea+=choa[g]
print(chea)
