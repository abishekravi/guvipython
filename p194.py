#a
A,B=map(str,input().split())
if A==B:
    print("D")
elif (A=="R" and B=="P") or (A=="P" and B=="R"):
    print("P")
elif (A=="S" and B=="P") or (A=="P" and B=="S"):
    print("S")
elif (A=="S" and B=="R") or (A=="R" and B=="S"):
    print("R")
