def generate_rectangle(n, m):
    a=[]
    if 1<=n and m<=100:
        for i in range(n):
            a.append(m*"*")
    return a
            
