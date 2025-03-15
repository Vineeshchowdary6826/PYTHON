def generate_square(n):
    b=""
    l=[]
    for i in range(n):
        b+="*"

    for i in range(n):
        l.append(b)
    return l
