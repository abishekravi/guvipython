#a
num,ques=map(str,input().split(" "))
count=0
for i in num:
    if(i==ques):
        count=count+1
print(count)
