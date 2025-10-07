from pyfiglet import Figlet
import random

colors = [
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m","\033[96m"
]
fonts = ["slant","block","banner3-D","isometric1",
         "standard","digital"]
text = input('Enter your text:') or 'Python Rocks!'
print('\nChoose a Font:')
for i, f in enumerate(fonts, 1):
    print(f"{i}. {f}")
choice = int(input("Enter font number:") or 1)
f = Figlet(font=fonts[choice-1])
banner = f.renderText(text)
print(random.choice(colors) + banner + "\033[0m")