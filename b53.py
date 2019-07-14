#a
i=0
Num = int(input(""))
S= 0
while(Num > 0):
    i= Num % 10
    S = S+i
    Num = Num //10
print(S)
