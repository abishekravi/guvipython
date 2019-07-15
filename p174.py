#a
A=input()
B=input()
C=['1:']
d=['2:']
if A.isnumeric()==False:
    A=A.split()
    B=B.split()
    for i in A:
        if i not in B:
            d.append(i)
    for i in B:
        if i not in A:
            C.append(i)
else:
    A=list(A)
    B=list(B)
    for i in range(0,max(len(A),len(B))):
        if i<min(len(A),len(B)) and A[i]!=B[i]:
            d.append(A[i])
            C.append(B[i])
        elif i>=min(len(A),len(B)):
            if max(len(A),len(B))==len(A):
                d.append(A[i])
            if max(len(A),len(B))==len(B):
                C.append(B[i])
if len(C)>1:
    print(*C,sep='')
if len(d)>1:
    print(*d,sep='')
