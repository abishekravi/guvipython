#a
N=input()
n=int(N,2)
while 1:
  if (n & (n-1)):
    n+=1
  else:
    print(n)
    break
