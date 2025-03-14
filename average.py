t = int(input())            
for i in range(t):          
    A, C = map(int, input().split())
    if (A%2!=0 and C%2!=0) or (A%2==0 and C%2==0):
        B=(A+C)//2
        print(B)
    else:
        print(-1)
    
