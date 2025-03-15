def generate_hollow_square(n):
    
    l=[]
    for i in range(n):
        if i==0 or i==(n-1):
            l.append(n*"*")
        else:
            l.append("*"+(n-2)*" "+"*")
    return l
            
