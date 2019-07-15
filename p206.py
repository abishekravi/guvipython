#a
N=input()
try:
    int(N,16)
    print("yes")
except ValueError:
    print("no")
