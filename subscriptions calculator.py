def Subscription(n):
    for i in range(n):
        N,X=map(int,input().split())
        if N>6:
            cost=(N//6)
            if N%6!=0:
                cost+=1
            print(cost*X)
        else:
            print(X)
n=int(input())
Subscription(n)
