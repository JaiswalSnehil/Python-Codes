n = int(input("Enter no. of rows: "))

for i in range(n, 0, -1):

    # spaces
    print(" " * (n - i), end="")

    # numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    print()