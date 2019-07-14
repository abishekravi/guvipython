#a
q=input()
count1=0
for j in q:
  if (j.isdigit() or j.isalpha()):
    count1+=1
if count1!=0:
  print("Yes")
else:
  print("No")
