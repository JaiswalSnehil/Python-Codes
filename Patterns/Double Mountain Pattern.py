n = int(input('Enter size of Mountain:'))

for i in range(1, n+1):
    print(
        " "*(n-i) +
        "* "*i +
        "  "*(n-i) +
        "* "*i
    )