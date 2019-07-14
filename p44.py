#a
num,k_shift=input().split()
k_shift=int(k_shift)

for i in range(k_shift):
    num=num[-1]+num[:-1]
print(num,end=' ')
