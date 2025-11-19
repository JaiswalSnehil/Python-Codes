def print_pascals_triangle(rows):
    for i in range(rows):
        # Print leading spaces
        print(" "*(rows-i), end=" ")

        # Initialize the first elementof each row as 1
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            # Update num to the next value in Passcal's Triangle
            num = num*(i-j)//(j+1)

        # Move to the next line after each row
        print()

# Example: Print Pascal's Triangle with 5 rows
print_pascals_triangle(5)