#a
from collections import Counter      #import the collection file we easily check by the anagram or not
string="kabali"

n=int(input())                      # get the input
values=[]
count=0
if  n>=1 and n<=1000:                #check the  constraint
    for i in range(n):
        values.append((input()))

for val in values:
    if Counter(val)==Counter(string):     #check the anagram or not
        count=count+1
print(count)
