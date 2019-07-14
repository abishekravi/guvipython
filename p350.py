#a
import sys,string, math,itertools

def minChCnt(s) :
    dic1 = {}
    for c in s :
        if not c.isspace() :
            dic1[c] = dic1.get(c,0) + 1
    min1 = sys.maxsize
    L = []
    min1 = min(dic1.values())
    for k,v in dic1.items() :
        if v == min1 :
            L.append(k)
    return L

s = input()
n = len(s)
L = minChCnt(s)
print(*L)
