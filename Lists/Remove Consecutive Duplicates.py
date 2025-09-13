# Remove consecutive duplicates from a List, preserving order 

from itertools import groupby

lst = [1, 2, 2, 3, 3, 3, 4, 4, 5]
result = [key for key, _ in groupby(lst)]
print(result)