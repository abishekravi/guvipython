#a
number_ob=int(input())
for i in range(2,number_ob):
    if(number_ob%i==0):
        print("yes")
        break
else:
    print("no")
