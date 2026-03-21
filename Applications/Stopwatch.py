import time
import sys
import select

print("Stopwatch started! Press 'q' + Enter to stop.")

start = time.time()

while True:
    elapsed = int(time.time() - start)
    mins, secs = divmod(elapsed, 60)

    sys.stdout.write(f"\rElapsed Time: {mins:02d}:{secs:02d}")
    sys.stdout.flush()

    time.sleep(1)

    # check if user typed something
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        if sys.stdin.readline().strip().lower() == 'q':
            break

print(f"\nStopwatch stopped at {mins:02d}:{secs:02d}")