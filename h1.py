n1 = int(input())
lst = [x for x in input().split()]
lst1 = []
for i in lst:
    if lst.count(i) > 1:
        lst1.append(i)
if len(lst1) == 0:
    print('unique')
else:
    print(' '.join(sorted(set(lst1))))
