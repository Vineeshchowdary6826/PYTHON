def generate_diamond(n):

    for i in range(1,n+1):
        stars=((2*i)-1) * "*"
        spaces=" " *(n-i)
        print(spaces,stars,spaces)
    for i in range(n-1,0,-1):
        stars=((2*i)-1) * "*"
        spaces=" " *(n-i)
        print(spaces,stars,spaces)

    
n=int(input())
generate_diamond(n)
