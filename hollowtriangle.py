def generate_hollow_right_angled_triangle(n):
    l=[]
    for i in range(1,n+1):
        if i==1 or i == 2 or i==n:
            l.append(i*"*")
        else:
            l.append("*"+(i-2)*" "+"*")
    return l
            
