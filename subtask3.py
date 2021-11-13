def myfunc(a,b):
    if b == 0:
        print(-1,-1)
    else:
        r = a
        q = 0
        while r>b:
            r = r-b
            q +=1
        print(q,r)
myfunc(9, 3)
