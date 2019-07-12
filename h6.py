 #a   
sandy1 = input()
san1 = list(map(int,input().split()))
tan1 = False
for i in san1:
    if san1.count(i) > 1:
        tan1 = True
        break
print(i if tan1 else "unique")
