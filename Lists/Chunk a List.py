# Split a list into evenly sized chunks

def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

lst = [1, 2, 3, 4, 5, 6, 7, 8]
chunks = list(chunk(lst, 3))
print(chunks)