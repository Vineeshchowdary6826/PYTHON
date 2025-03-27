def is_palindromic_tuple(tup):
    l=[]
    m=[]
    for i in tup:
        l.append(i)
    for j in reversed(tup):
        m.append(j)

    if l==m:
        return True
    else:
        return False
