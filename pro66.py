#a
w, x, y, z = map(int,input().split())
count = 0
x1 = x-y
if(x1 >= 0):
    di = (w-y)*2
    for i in range(z):
        if(i == z-1):
            di = di/2
        if(x1 < di):
            x1 = x
            count += 1
        x1 = x1-di
        if(x1 < 0):
            count = -1
            break
        di = 2*w-di
    print(count)
else:
    print(-1)
