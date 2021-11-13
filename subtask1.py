def findnum(n):
    b=0
    a=1
    while (b**2 > n or n>=a**2):
        b+=1
        a+=1
    q=b**2
    print(q)
