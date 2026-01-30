from rich.live import Live
from rich.text import Text
import time

frames = ["◐", "◓", "◑", "◒"]

with Live(refresh_per_second=10) as live:
    i = 0
    while True:
        live.update(
            Text(frames[i % 4] * 10, style="bold magenta")
        )
        i += 1
        time.sleep(0.2)
