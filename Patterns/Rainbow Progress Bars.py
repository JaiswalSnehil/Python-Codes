import time
from itertools import cycle

colors = cycle(["\033[91m","\033[93m",
                "\033[92m","\033[06m",
                "\033[94m","\033[95m"])
length = 50

for i in range(length+1):
    bar = "".join(next(colors) + "█" for _ in range(i))
    print(f"\r{bar:<50}", end="")
    time.sleep(0.1)
print("\nDone!")