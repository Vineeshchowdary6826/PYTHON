def generate_inverted_pyramid(n):
    
    l=[]
    for i in range(n):
        stars=(2*(n-i)-1)*"*"
        spaces=" "*i
        l.append(spaces+stars+spaces)
    return l
n=int(input())
result = generate_inverted_pyramid(n)
for row in result:
    print(row)
