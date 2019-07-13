#a
inp=list(input())
final=[]
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in inp:
    if i=='X':
        final.append("A")
    elif i=='Y':
        final.append("B")
    elif i=="Z":
        final.append("C")
    else:
        final.append(letter[letter.index(i)+3])
print("".join(final))
