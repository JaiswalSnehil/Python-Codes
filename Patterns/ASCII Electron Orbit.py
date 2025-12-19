import math, time, os

for t in range(15):
    pos = int(20*math.sin(t/3)+20)
    print(" "*pos + "e⁻")
    time.sleep(0.1)
    os.system("cls" if os.name=="nt" else "clear")