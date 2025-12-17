import time, os

a, b = 0, 1
for _ in range(15):
    print(" "*b + str(a))
    a, b = b, a+b
    time.sleep(0.3)
    os.system("cls" if os.name=="nt" else "clear")