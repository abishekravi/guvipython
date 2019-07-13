#a
A,B=input().split()
temp=""
def string(n):
   x=""
   for i in range(1,n+1):
      x+=str(i)
   return x
if len(B)>len(A):
   A+=string(len(B)-len(A))
elif len(A)>len(B):
   B+=string(len(A)-len(B))
for i in range(len(A)):
   temp+=(A[i]+B[i])
print(temp)
