#a
x=input()
y=0
for i in range(len(x)):
    if (x[i].isalpha() or x[i].isnumeric() or x[i]==" "):
      continue
    y=y+1
else:
    print(y)
