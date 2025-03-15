def generate_triangle(n):

    l=[]
    a=""
    for i in range(n):
        a+="*"
        l.append(a)
    for i in l:
        print(i)
n=int(input("rows:"))        
generate_triangle(n)
