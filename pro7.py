chatr=int(input())
gr=[]
dog=0
for h in range (0,chatr+1):
    dog=abs((2**h)-chatr)
    gr.append(dog)
kall=min(gr)
print(kall)
