import psutil
import time

before = psutil.net_io_counters()
time.sleep(1)
after = psutil.net_io_counters()

download = after.bytes_recv - before.bytes_recv
upload = after.bytes_sent - before.bytes_sent

print("Download speed:", download, "Bytes/sec")
print("Upload speed:", upload, "Bytes/sec")