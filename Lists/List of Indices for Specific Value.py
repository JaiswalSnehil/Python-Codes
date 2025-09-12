# Get all indices of a specific value in a list

lst = [10, 20, 10, 30, 10, 40]
indices = [i for i, x in enumerate(lst) if x==10]
print(indices)
