def rotate(lst, n):
    return lst[-n:] + lst[:-n]

lst = [1, 2, 3, 4, 5]
rotated_list = rotate(lst, 2)
print(rotated_list)