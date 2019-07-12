n12 = int(input())
s12 = [x for x in input().split()]
t12 = []
for i in range(len(s1)):
    if s12[i] == str(i):
        t1.append(s1[i])

if len(t12) == 0:
    print('-1')
else:
    print(' '.join(sorted(t12)))
