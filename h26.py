#a
n=int(input())
fin=[]
l=list(map(int,input().split()))[:n]
fin=l.reverse()
print(*l,sep='->')
