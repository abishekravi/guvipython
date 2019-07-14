#a
number=int(input())
for power in range(100):
    if(number==2**power):
        print("yes")
        break
else:
    print("no")
