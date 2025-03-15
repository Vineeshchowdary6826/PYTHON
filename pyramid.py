def generate_pyramid(n):
    pyramid=[]
    for i in range(1,n+1):
        stars=(2*i-1)*'*'
        spaces=" "*(n-i)
        pyramid.append(spaces+stars+spaces)
    return pyramid
        
n=int(input())
print(generate_pyramid(n))

