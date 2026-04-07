rows = int(input('Enter no. of Rows:'))
cols = int(input('Enter no. of Columns:'))

for i in range(rows):
    for j in range(cols):
        if (i+j)%2 == 0:
            print('X', end=' ')
        else:
            print('O', end=' ')
    print()