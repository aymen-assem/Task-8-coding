def seq(*i):
    s=0
    sequence=[]
    if len(i)==0:
        print("n=0, m=-1, a=-1")
    else:
        for x in i:
            if x!=-1:
                sequence.insert(0, x)
                s+=x
            else:
                break
        m= min(sequence)
        n= len(sequence) 
        a= s / n
        print(s, m, n, a)
