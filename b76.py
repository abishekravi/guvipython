#a
inter=int(input())
if inter>1:
    for i in range(2,inter):
        if(inter%i)==0:
            print("yes")
            break
    else:
        print("no")
