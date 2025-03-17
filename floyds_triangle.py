def generate_floyds_triangle(n):
    l=[]
    num=1
    for i in range(1,n+1):
        row=[]
        for j in range(i):
            row.append(str(num))
            num+=1
        l.append(" ".join(row))
       
    return l  
n=int(input("enter number:"))
for ele in (generate_floyds_triangle(n)):
    print(ele)
