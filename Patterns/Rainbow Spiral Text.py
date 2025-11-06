import time

text = "Python is fun!"
colors = [31, 32, 33, 34, 35, 36, 37]

for i in range(10):
    line = ""
    for idx, char in enumerate(text):
        color_code = colors[(idx + i) % len(colors)]
        line += f"\033[1;{color_code}m{char}\033[om"
    print(line)
    time.sleep(0.3)