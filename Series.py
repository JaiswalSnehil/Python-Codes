# Decreasing series with the differences being in GP and values should be greater than 100

def series(n):
    i = 0
    l = []
    while n > 100:
        if n-i > 100:
            l.append(n-i)
        n -= i
        i += 1
    
    for i in l:
        print(i, end = ' ')

series(200)