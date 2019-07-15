#a
A,B,C=map(int,input().split())
if A+B>=C and B+C>=A and C+A >=B:
    print("yes")
else:
    print("no")
