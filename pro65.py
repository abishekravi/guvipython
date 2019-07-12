#a
a,b = map(int,input().split())
x = list(map(int,input().split()))
y = int(input())
z = (sum(x)-x[b])//2
if y==z:
  print("Bon Appetit")
else:
  print(y-z)
