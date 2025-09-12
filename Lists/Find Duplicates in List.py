# Identify duplicate elements in a List

from collections import Counter

lst = [1, 2, 2, 3, 4, 4, 4, 5]
duplicates = [item for item, count in Counter(lst).items() if count>1]
print(duplicates)
