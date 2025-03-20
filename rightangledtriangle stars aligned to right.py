def generate_right_angled_triangle(n):
    l=[]
    for i in range(1,n+1):
        stars="*" *i
        spaces=" " * (n-i)
        l.append(spaces+stars)
    return l
