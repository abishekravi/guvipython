#a
N=str(input())
for i in range(len(N)):
    if(N[i].islower()==True):
        print(N[i].upper(),end="")
    else:
        print(N[i].lower(),end="")
