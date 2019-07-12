#a
s=['1','2','3','4','5','6','7','8','9','0']
n=input()
n=(list(n))
a=0
for i in range(0,len(n)):
    if a>0: i=i-a
    if n[i] in s:
        n[i]=int(n[i])
    if type(n[i-1])==int and type(n[i])==int:
        n[i-1]=int(str(n[i-1])+str(n[i]))
        n.pop(i)
        a=a+1
for i in range(0,len(n),2):
    if n[i+1]%2==0:
        print(n[i]*n[i+1],end="")
    else:
        print(n[i],end="")
        print(n[i+1],end="")
