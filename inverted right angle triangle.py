def generate_inverted_triangle(n):

    for i in range(n, 0, -1):  # Start at n, decrease to 1
        print("*" * i)  # Print '*' i times


n = int(input("Enter the size of the inverted triangle: "))
generate_inverted_triangle(n)
