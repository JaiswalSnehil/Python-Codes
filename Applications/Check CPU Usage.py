import psutil

cpu_percent = psutil.cpu_percent(interval=1)
print("CPU usage:", cpu_percent, "%")