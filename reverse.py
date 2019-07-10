def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = "Geeksforgeeks"
  
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 
