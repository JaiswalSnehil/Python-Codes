def print_pyramid(rows):
    for i in range(1, rows+1):
        # Print leading spaces
        print(" "*(rows-i), end="")

        # Print numbers in increasing order
        for j in range(1,i+1):
            print(j, end=" ")

        # Move to the next line
        print()

print_pyramid(5)