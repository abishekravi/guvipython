#a
a1 = int(input())
while a1%10==0:
    a1=a1//10
a1=str(a1)
b=a1[::-1]
if a1==b:
    print("yes")
else:
    print("no")
