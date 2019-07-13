#a
no_of_elements,shift_count=map(int,input().split())

list_of_elements=list(map(int,input().split()))
for i in range(shift_count):
    list_of_elements=[list_of_elements[-1]]+list_of_elements[:-1]
print(*list_of_elements,end=" ")
