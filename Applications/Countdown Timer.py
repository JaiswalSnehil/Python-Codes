import time

seconds = int(input("Enter seconds for countdown:"))
for i in range(seconds,0,-1):
    print(f"Time left: {i} second",end="\r")
    time.sleep(1)

print("Time's up! ⏰")