#a
number=int(input())
list1=[]
for i in range(2,number+1):
    if(number%i==0):
        list1.append(i)
for num in list1:
    if(num%2==0):
        print(num,end=" ")
