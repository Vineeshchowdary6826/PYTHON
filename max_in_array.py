t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    maximum = arr[0]
    for i in range(1, n):
        if arr[i] > maximum:
            maximum = arr[i]
    
    print(maximum)
