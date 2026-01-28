import os

title = input("Notification title: ")
msg = input("Notification message: ")

os.system(f'''osascript -e 'display notification "{msg}" with title "{title}"' ''')